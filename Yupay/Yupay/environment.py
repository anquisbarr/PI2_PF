import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
POST_URL = os.getenv("URL_POST_STAMP")
GET_URL = os.getenv("URL_GET_STAMP")
