import base64
import requests

CLIENT_ID = 'f0cd9a2febaf4bd792d39b86430a442d'
CLIENT_SECRET = '8b428da3e1354ad9b18c14caa5e7fea5'
main_string = CLIENT_ID +':'+ CLIENT_SECRET


#making string connection
main_string_bytes = main_string.encode('ascii')
main_string_base64_bytes = base64.b64decode(main_string_bytes)
main_string_base64 = main_string_base64_bytes.decode('ascii')

STRING_FOR_TOKEN = main_string_base64
REQUEST_URL = 'https://accounts.spotify.com/api/token'

def get_token():#have to  take the access token 
    headers = {
        'Authorization': 'Basic' + STRING_FOR_TOKEN,
        'Content-Type':'application/x-www-form-urlenconded'
    }
    data = {'grant_type':'client_credetials'}
    response = requests.request('POST',url = REQUEST_URL, headers = headers, data = data)

    access_token = response.json()['access_token']
    return access_token


