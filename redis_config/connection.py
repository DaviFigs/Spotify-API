import redis
cache_redis = redis.Redis(host='localhost', port=6379, db=0)

access_token = cache_redis.get('access_token')
print(access_token)