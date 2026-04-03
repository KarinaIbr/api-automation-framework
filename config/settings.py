import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
AUTH_SECRET = os.getenv("AUTH_SECRET")
TIMEOUT = 10