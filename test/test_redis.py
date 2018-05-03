import redis

r = redis.Redis(host="123.206.190.67",port=6379,db=0)
r.set('hello','world')
print(r.get('hello'))