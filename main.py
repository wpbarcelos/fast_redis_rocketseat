import redis
redis_conn = redis.Redis(host="localhost", port=6379, db=0)

redis_conn.set('mykey', 'foo')

redis_conn.delete('minha_chave')

response = redis_conn.get('minha_chave').decode('utf-8')
print(response)
