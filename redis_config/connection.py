import redis
R = redis.Redis(host='localhost', port=6379, db=0)

top10_tracks = R.get('top10_tracks')
top10_artists = R.get('top10_artists')

test = R.hset('user:123',mapping={
    'name':'nance',
    'email':'nance@hotmail.com'
})

print(R.hgetall('user:123'))
R.delete('Test')
R.delete('accesss_token')
R.delete('access_token')
R.delete('user:123')



