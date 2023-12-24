import base64
import requests
import os 
from dotenv import load_dotenv

load_dotenv()


main_string = os.getenv('CLIENT_ID') +':'+ os.getenv('CLIENT_SECRET')


#making string connection
main_string_bytes = main_string.encode('ascii')
main_string_base64_bytes = base64.b64encode(main_string_bytes)
main_string_base64 = main_string_base64_bytes.decode('ascii')

STRING_FOR_TOKEN = main_string_base64
REQUEST_URL = 'https://accounts.spotify.com/api/token'

#we cannot use this token to access the user data
def get_token():
    header = {
        'Authorization':f'Basic {main_string_base64}',
        'Content-type':'application/x-www-form-urlencoded'
    }
    body = {
        'grant_type':'client_credentials'
    }
    response = requests.request('post', url=REQUEST_URL, headers= header, data = body)
    return response


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


