import base64
import requests
import os 
from dotenv import load_dotenv
load_dotenv()


main_string = os.getenv('CLIENT_ID')+':'+os.getenv('CLIENT_SECRET')

main_string_bytes = main_string.encode('ascii')
main_string_bytes_64 = base64.b64encode(main_string_bytes)
final_string_base64 = main_string_bytes_64.decode('ascii')

REQUEST_STRING = final_string_base64



def callbacks(code):
    body={
        'grant_type':'authorization_code',
        'code':code,
        'redirect_uri':os.getenv('CALLBACK_URL'),
    }
    header={
        'Authorization':'Basic '+REQUEST_STRING,
        'content-type':'application/x-www-form-urlencoded'
    }
    response = requests.post(os.getenv('REQUEST_TOKEN_URL'), headers=header, data=body)
    return response.json()

#Vamos testar agora nas views


