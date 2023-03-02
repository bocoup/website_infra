import base64

import requests

from env import ENVIRONMENT

wordpress_username = ENVIRONMENT.get("wordpress_username")
wordpress_password = ENVIRONMENT.get("wordpress_password")
wordpress_credentials = wordpress_username + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {"Authorization": "Basic " + wordpress_token.decode('utf-8')}

#TODO make environment variable
base_url = "http://bocouptest.local:57973/wp-json/wp/v2/"

def get_total_pagecount(url:str):
    response = requests.get(url)
    pages_count = response.headers['X-WP-TotalPages']
    return int(pages_count)

def get_posts(post_type:str, parameters:str):
    current_page = 1
    api_url = base_url + post_type + f"?perPage=100&page={current_page}&" + parameters 
    total_pages = get_total_pagecount(api_url)

    all_responses_raw = []

    while current_page <= total_pages:
        api_url = base_url + post_type + f"?perPage=100&page={current_page}&" + parameters 
        current_page += 1
        response = requests.get(api_url)
        response_json = response.json()
        all_responses_raw.append(response_json)
    
    all_responses = [item for sublist in all_responses_raw for item in sublist]
    
    return all_responses

def update_post(post_type:str,post_id:str, post_data:dict):
    api_url = base_url + post_type + "/" + post_id
    #response = requests.post(api_url, auth=(wordpress_username, wordpress_password), json=post_data)
    
    # Bocoup work url needs to be working in order for us to POST
    print(api_url)
    response = requests.options(api_url, auth=(wordpress_username, wordpress_password))

    # Running into 401
    # {'code': 'rest_cannot_edit', 'message': 'Sorry, you are not allowed to edit this post.', 'data': {'status': 401}}
    print(response.json())
    exit