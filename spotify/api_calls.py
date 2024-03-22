import os
from dotenv import load_dotenv
import requests
load_dotenv()
BASE_TOP_URL = os.getenv('BASE_TOP_URL')


def call_api( access_token, action, time,limit):
    headers = {
        'Authorization':'Bearer '+ access_token
    }
    request_url = filtering(action, time, limit)
    response = requests.get(url=request_url, headers=headers)
    return response.json()
    

#This def will take the filter witch we did, and will build our request_url
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
        return '25'
    elif limit == '3':
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

def create_message(action,time,limit):
    action = filter_action(action)
    time = filter_time(time)
    limit = filter_limit(limit)

    if action == 'artists':
        if time == 'short_term':
            message = f'These are your top {limit} artists from last month'
        if time =='medium_term':
            message = f'These are your top {limit} artists from last 6 months'
        if time =='long_term':
            message = f'These are your top {limit} artists of all time'
        return message

    else:  
        if time == 'short_term':
            message = f'These are your top {limit} tracks from last month'
        if time =='medium_term':
            message = f'These are your top {limit} tracks from last 6 months'
        if time =='long_term':
            message = f'These are your top {limit} tracks of all time'
        return message  