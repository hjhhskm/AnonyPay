import redis
import time

r = redis.Redis(host="123.206.190.67",port=6379,db=0)
r.set('hello','world1')
index = 1
print(r.get('hello'))
if r.get('world') == None:
    print("good")
print(r.get("world"))

nowtime = 1102
r.set(str(index)+"time",nowtime)
nowtime = r.get(str(index)+"time")
print(nowtime)

r.set(str(index)+"time",int(nowtime)+1)
nowtime = r.get(str(index)+"time")
print(nowtime)
