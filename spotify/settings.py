import base64
import requests
import os 
from dotenv import load_dotenv
load_dotenv()


def callbacks(code):
    body = {
        'code':code,
        'grant_type':'authorization_code',
        'redirect_uri':os.getenv('CALLBACK_URL'),
        'client_id':os.getenv('CLIENT_ID'),
        'client_secret':os.getenv('CLIENT_SECRET')
    }
    response = requests.post(os.getenv('REQUEST_URL'), data=body)
    return response.json()


