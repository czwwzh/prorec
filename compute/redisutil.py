#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import redis
import time

from computeconfiguration import  *


class Redis_db:
    RedisInfo = REDIS_CONNECT_INFO
    RedisConn = None

    __RedisData = 'recommend_data'

    def __init__(self):
        self.link_redis()

    def link_redis(self,num = 0):
        conf = self.RedisInfo
        # print('connect redis'),
        self.RedisConn = redis.Redis(**conf)
        try:
            self.RedisConn.ping()
            # print('--->Success')
            return True
        except redis.exceptions.ConnectionError as e:
            # print('ERROR:'+str(e),'Redis')
            time.sleep(1)
            num+=1
            if num < 2:
                self.link_redis(num)
            return False

    def GetList(self):
        try:
            self.RedisConn.ping()
            _,json = self.RedisConn.blpop(self.__RedisData)
        except TypeError as e:
            # print('ERROR:' + str(e))
            res = self.link_redis()
            if res == False:
                # print('GETLIST:CLOSE CONNECT REDIS')
                return res
            json = self.RedisConn.blpop(self.__RedisData)
        return json

    def RpushData(self,string):
        try:
            self.RedisConn.ping()
            self.RedisConn.rpush(self.__RedisData, string)
        except redis.exceptions.ResponseError as e:
            # print('ERROR:' + str(e))
            #self.__Obj.WriteLog('ERROR:' + str(e), 'Redis')
            res = self.link_redis()
            if res == False:
                # print('GETLIST:CLOSE CONNECT REDIS')
                #self.__Obj.WriteLog('GETLIST:CLOSE CONNECT REDIS', 'Redis')
                return res
            self.RedisConn.rpush(self.__RedisData, string)