import redis
import json
R = redis.Redis(host='localhost', port=6379, db=0)

top10_tracks = R.get('top10_tracks')
top10_artists = R.get('top10_artists')

test = R.hset('user:123',mapping={
    'name':'nance',
    'email':'nance@hotmail.com'
})

'''all_user_data ={ 
    'top10_track_lm': [
        {'name':'NAME', 'artist':'ARTIST', 'album':'ALBUM','duration':'1222'}],
    
    'top10_track_l6': [
        {'name':'NAME', 'artist':'ARTIST', 'album':'ALBUM', 'duration':'2212'},
    ],

    'top10_track_at': [
        {'name':'NAME', 'artist':'ARTIST', 'album':'ALBUM', 'duration':'3030'},
    ],
}
all_user_data = json.dumps(all_user_data)

teste2 = R.hset('top_things', 'user_data',all_user_data)

print(R.hgetall('top_things'))
print(all_user_data)'''



