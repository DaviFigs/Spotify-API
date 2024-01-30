import redis
cache_redis = redis.Redis(host='localhost', port=6379, db=0)

top10_tracks = cache_redis.get('top10_tracks')
top10_artists = cache_redis.get('top10_artists')

print(top10_tracks)
print(top10_artists)




