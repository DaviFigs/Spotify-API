from settings import get_token, get_user_token
import requests

url_user = 'https://api.spotify.com/v1/me'

#token = get_token().json()['access_token']
headers = {'Authorization':'Bearer '+ get_token().json()['access_token']}

response_user = requests.request('GET', url = url_user, headers=headers)

response_user.status_code

print(response_user.json())


response = get_user_token()
print(response.json())
