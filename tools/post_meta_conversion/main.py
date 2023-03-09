
from acf_functions import convert_post_meta_fields_to_acf_fields
from block_functions import convert_post_meta_fields_to_block_fields
from constants import POST_TYPES
from csv_functions import get_post_csv_data, load_csv_data
from wordpress_functions import get_posts, update_post
import json

#1. Grab and load the meta data from the database
csv_data = load_csv_data("./post_meta_data.csv")

post_type_map = {
    'bocoup_work': 'work'
}

for post_type in POST_TYPES:

    #2. get all the posts of post type from wordpress
    posts = get_posts(post_type, "")
    
    for post in posts:

        #3. grab the posts meta data
        post_csv_data_rows = get_post_csv_data(csv_data, "post_id", post.get("id"))
        
        #4. convert the meta data into acf fields
        acf_fields = convert_post_meta_fields_to_acf_fields(post_type, post_csv_data_rows)

        #5. update the post through the REST API
        update_post(post_type, str(post.get("id")), acf_fields)