import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('Test', 'test')

print(r.get('Test'))