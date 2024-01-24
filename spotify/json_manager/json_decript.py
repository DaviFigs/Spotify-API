#Here I'll make functions wich receive json and organize them
from .item_list import SongItem, ArtistItem
import time 
  

def convert(seconds): 
    if seconds < 3600:
        return time.strftime("%M:%S", time.gmtime(seconds))
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def get_tracks_info(json_response):
    cont=1
    response_items = []
    tracks_list = json_response['items']

    for i in tracks_list:
        number = cont
        image = i['album']['images'][0]['url']
        album = i['album']['name']
        artist = i['artists'][0]['name']
        duration = (i['duration_ms']/1000)
        name = i['name']
        link = i['external_urls']['spotify']
        
        duration = convert(duration)
        
        track = SongItem(number,link, name, album, artist, duration, image)
        response_items.append(track)
        cont+=1
        
    return response_items
        

def get_artists_info(json_response):
    cont = 1
    response_items = []
    artist_list = json_response['items']

    for i in artist_list:
        number = cont
        image = i['images'][0]['url']
        link = i['external_urls']['spotify']
        name = i['name']
        popularity = i['popularity']
        artist = ArtistItem(number,link,name, popularity, image)
        response_items.append(artist)
        cont+=1

    return response_items