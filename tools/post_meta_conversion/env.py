import os

from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = {
    "wordpress_username": os.getenv("wordpress_username"),
    "wordpress_password": os.getenv("wordpress_password")
}