import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN1 = os.getenv("ACCESS_TOKEN1")
ACCESS_TOKEN2 = os.getenv("ACCESS_TOKEN2")
POST_URL = os.getenv("URL_POST_STAMP")
GET_URL = os.getenv("URL_GET_STAMP")
