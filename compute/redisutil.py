#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from configurationlocal import *
import redis

class Redis_db:

    RedisInfo = REDIS_CONNECT_INFO
    RedisConn = None

    def __init__(self,rdsdata = 'recommend_data'):
        self.__RedisData = rdsdata
        self.link_redis()

    def link_redis(self):
        conf = self.RedisInfo
        ist = True
        print('connect redis',)
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

    def SetData(self, uuid, data=None, ist=False):
        if data == None:
            ist = True
        try:
            self.RedisConn.ping()
        except redis.exceptions.ResponseError as e:
            print('ERROR:' + str(e))

        if ist == False:
            self.RedisConn.set(uuid, data)
        else:
            res = self.RedisConn.get(uuid)
            self.RedisConn.delete(uuid)
            return res