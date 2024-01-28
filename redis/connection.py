import redis
cache_redis = redis.Redis(host='localhost', port=6379, db=0)

cache_redis.set('access_token', 'none' ,3600)