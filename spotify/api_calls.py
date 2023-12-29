import os
from dotenv import load_dotenv
import requests
load_dotenv()
BASE_TOP_URL = os.getenv('BASE_TOP_URL')
    #example = 'https://api.spotify.com/v1/me/top/tracks?offset=0&limit=10&time_range=short_term'
    #example2= 'https://api.spotify.com/v1/me/top/tracks?offset=0&limit=10&time_range=short_term


def call_api( access_token, action, time,limit):
    headers = {
        'Authorization':'Bearer '+ access_token
    }
    request_url = filtering(action, time, limit)
    response = requests.get(url=request_url, headers=headers)
    #response = requests.get(url= 'https://api.spotify.com/v1/me', headers=headers)
    #WE ARE GETITNG PROBLEMS IN AUHTENTIACATION, OUR LEVEL OF AUTHENTICATION IS NOT ALLOWED TO GET USER DATA
    return response.json()
    

def filtering(action, time,limit):
    offset = '0'
    limit = filter_limit(limit)
    action = filter_action(action)
    time = filter_time(time)

    request_url = f'{BASE_TOP_URL}/{action}?offset={offset}&limit={limit}&time_range={time}'
    return request_url

def filter_limit(limit):
    if limit == '1':
        return '10'
    elif limit == '2':
        return '50'

def filter_action(action):
    if action == '1':
        return 'artists'
    elif action == '2':
        return 'tracks'
    

def filter_time(time):
    if time == '1':
        return 'short_term'
    elif time =='2':
        return 'medium_term'
    elif time == '3':
        return 'long_term'

