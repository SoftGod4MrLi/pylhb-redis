"""
模块：myredis
作者：李生
描述：Redis操作
"""
import redis

class MyRedis:
    def __init__(self,host="localhost",port=6379,password="",db=0):
        if len(password)==0:
            self.redis = redis.Redis(host=host, port=port,db=db,decode_responses=True)
        else:
            self.redis = redis.Redis(host=host, port=port,password=password, db=db,decode_responses=True)
        pass

    # 键值对处理
    def set(self,key,value,seconds=0):
        if seconds==0:
            self.redis.set(key,value)
        else:
            self.redis.setex(key,seconds,value)
    def get(self,key,defaultValue=None):
        if self.redis.exists(key):
            return self.redis.get(key)
        else:
            return defaultValue
    def delete(self,key):
        self.delete(key)
    def expire(self,key,seconds):
        self.redis.expire(key,seconds)

    # 哈希表处理
    def hset(self,name,data:set):
        self.redis.hset(name,mapping=data)
    def hget(self,name,key,defaultValue=None):
        if self.redis.hexists(name,key):
            return self.redis.hget(name,key)
        else:
            return defaultValue
        
    # 列表处理
    def lpush(self,key,data:list):
        for d in data:
            self.redis.lpush(key,d)
    def rpush(self,key,data:list):
        for d in data:
            self.redis.rpush(key,d)
    def lrangle(self,key,start=0,end=-1):
        return self.redis.lrange(key,start,end)
    
    # 集合处理（去重列表）
    def sadd(self,key,data:list):
        for d in data:
            self.redis.sadd(key,d)
    def smemebers(self,key):
        return self.redis.smembers(key)

    # 遍历所有键
    def fetchAll(self):
        keys=self.redis.keys("*")
        for key in keys:
            kType=self.redis.type(key)
            if kType=="string":
                value=self.redis.get(key)
            elif kType=="list":
                value=self.redis.lrange(key,0,-1)
            elif kType=="hash":
                value=self.redis.hgetall(key)
            elif kType=='set':
                value=self.redis.smembers(key)
            elif kType=="zset":
                value = self.redis.zrange(key, 0, -1, withscores=True)
            print(key,kType,value)

    # 清除所有键
    def flushall(self):
        self.redis.flushall()
