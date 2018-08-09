#coding=utf-8

#@Time      17-12-11 下午1:14
#@Auther    IISNT
import redis

class Redis_db:

    RedisInfo = {'host':'127.0.0.1','port':6379,'db':1}
    RedisConn = None


    def __init__(self,rdsdata = 'recommend_data'):
        self__RedisData = rdsdata
        self.link_redis()

    def link_redis(self):
        conf = self.RedisInfo
        ist = True
        print('connect redis'),
        self.RedisConn = redis.Redis(**conf)
        try:
            self.RedisConn.ping()
            print('--->Success')
        except redis.exceptions.ConnectionError as e:
            print('ERROR:'+str(e),'Redis')
            ist = False

        return ist

    def GetList(self):
        try:
            self.RedisConn.ping()
            _,json = self.RedisConn.blpop(self.__RedisData)
        except TypeError as e:
            print('ERROR:' + str(e))
            json = None
        return json

    def RpushData(self,string):
        try:
            self.RedisConn.ping()
            self.RedisConn.rpush(self.__RedisData, string)
        except redis.exceptions.ResponseError as e:
            print('ERROR:' + str(e))

    def LenData(self):
        llen = 0
        try:
            self.RedisConn.ping()
            llen = self.RedisConn.llen(self.__RedisData)
        except redis.exceptions.ResponseError as e:
            print('ERROR:' + str(e))

        return llen