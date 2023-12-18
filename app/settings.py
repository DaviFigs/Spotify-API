import base64

CLIENT_ID = 'f0cd9a2febaf4bd792d39b86430a442d'
CLIENT_SECRET = '8b428da3e1354ad9b18c14caa5e7fea5'
main_string = CLIENT_ID +':'+ CLIENT_SECRET


#making string connection
main_string_bytes = main_string.encode('ascii')
main_string_base64_bytes = base64.b64decode(main_string_bytes)
main_string_base64 = main_string_base64_bytes.decode('ascii')

REQUEST_URL = 'https://accounts.spotify.com/api/token'

def get_token():#have to  take the access token 


