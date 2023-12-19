from settings import get_token
import requests

url = 'https://api.spotify.com/v1/tracks/3T8Ht5f3xUejqEctN3RGb6'

token = get_token().json()['access_token']
headers = {'Authorization':f'Bearer {token}'}

response = requests.request('GET', url = url, headers=headers)
response.status_code

print(response.json())