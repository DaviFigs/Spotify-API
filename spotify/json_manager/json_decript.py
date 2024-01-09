#Here I'll make functions wich receive json and organize them
from .item_list import SongItem, ArtistItem

def get_tracks_info(json_response):
    response_items = []
    songs_list = json_response['items']
    
    for i in json_response['itens']:
        pass

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