#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import requests
# local
from dataetl.dataetlconfiguration import *
from dataetl.redisutil import Redis_db as rds
from dataetl.preprocessetlfunc import *
from dataetl.logutil import logger

# online
# from dataetlconfiguration import *
# from redisutil import Redis_db as rds
# from preprocessetlfunc import *
# from logutil import logger


class readClass:
    def __init__(self):
        pass
    def StartRun(self,uuid):

        print(type(uuid))
        print(uuid)
        my_rds = rds('recommend_data_msg')
        json_str = my_rds.SetData(uuid)
        json_str = json_str.decode()
        print(type(json_str))
        print(json_str)
        # print('1.data input time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        logger.info('1.data input time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


        # get data one by one
        ist = True
        try:
            key = uuid
            # print(key)
            logger.info(key)
            sourcedata = json_str
            # print(type(sourcedata))
            # print(sourcedata)
        except:
            ist = False

        if ist == False:
            self.sendtowx(uuid)
            return

        # sourcedata save
        res = footdatasavemysql(key, sourcedata)
        # data dataetl
        if res > 0:
            print('2.data save to mysql time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            logger.info('2.data save to mysql time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # filter data which is not str type
            res1 = streamstr(key, sourcedata)
            print('3.filter data which is not str type time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            logger.info('3.filter data which is not str type time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if res1 == False:
                self.sendtowx(uuid)
                return

            # filter data which is not json type
            res2 = streamjson(key, sourcedata)
            # print(res2)
            print('4.filter data which is not json type time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            logger.info('4.filter data which is not json type time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if res2 == False:
                self.sendtowx(uuid)
                return

            # transform data to json
            data = json.loads(sourcedata.replace('''"{''', "{").replace('''}"''', "}").replace('''\\''', '').replace("b'","").replace("n'",""))
            print('5.transform data to json time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            logger.info('5.transform data to json time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            # filter abnormal foot data
            res3 = footfilter(key, data)
            print('6.filter abnormal foot data time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            logger.info('6.filter abnormal foot data time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if res3 == False:
                self.sendtowx(uuid)
                return

                # get foot data in demend
            data = getFootData(data)
            uuid = data[1]['UUID']
            print('7.get foot data in demend time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            logger.info('7.get foot data in demend time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # get last data by shopno_sex and foot connect last
            data = footconnectlast(data)
            print('8.get last data by shopno_sex and foot connect last time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                time.localtime()))
            logger.info('8.get last data by shopno_sex and foot connect last time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                time.localtime()))
            # foot and last data dataetl save and send to redis
            res = footlastetlsave(data)
            if res > 0:
                # send uuid
                new_my_rds = rds()
                new_my_rds.RpushData(uuid)
                print(uuid,'--->success,send to redis')
            else:
                repetitivedatasave(uuid, sourcedata)
                self.sendtowx(uuid)
            print(
                '9.foot and last data dataetl save to mysql and send to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                   time.localtime()))
            logger.info('9.foot and last data dataetl save to mysql and send to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                                   time.localtime()))
        else:
            repetitivedatasave(key, sourcedata)
            self.sendtowx(uuid)

    def sendtowx(self,uuid):
        returndata = {'uuid': uuid,'res': -1}
        print(returndata)
        a = requests.post(RETURN_PORT_URL, data=returndata)
        print(a)

