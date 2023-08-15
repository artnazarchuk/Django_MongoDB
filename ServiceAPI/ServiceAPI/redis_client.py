import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
redis_client.set('test_key2', 'test_value2')
print(redis_client.get('test_key2'))
