#Here I'll make functions wich receive json and organize them
from .item_list import SongItem, ArtistItem
import time 
  
def convert(seconds): 
    if seconds < 3600:
        return time.strftime("%M:%S", time.gmtime(seconds))
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def get_tracks_info(json_response):
    response_items = []
    tracks_list = json_response['items']

    for i in tracks_list:
        album = i['album']['name']
        artist = i['artists'][0]['name']
        duration = (i['duration_ms']/1000)
        name = i['name']
        link = i['external_urls']['spotify']
        duration = convert(duration)
        
        track = SongItem(link, name, album, artist, duration)
        response_items.append(track)
        
    return response_items
        

def get_artists_info(json_response):
    response_items = []
    artist_list = json_response['items']

    for i in artist_list:
        link = i['external_urls']['spotify']
        name = i['name']
        popularity = i['popularity']
        artist = ArtistItem(link,name, popularity)
        response_items.append(artist)

    return response_items