#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import pandas
import requests
import json


# local
from compute.compute_etl_func import *
from compute.util_log import logger
from compute.util_redis import Redis_db as rds
from compute.compute_configuration import *


# online
# from computeetlfunc import *
# from util_log import logger
# from util_redis import *
# from compute_configuration import *


# =============================================================================
# load model and function
# suit
# model
model2 = pandas.read_pickle(SUIT2MODELPATH)
model6 = pandas.read_pickle(SUIT6MODELPATH)
model12 = pandas.read_pickle(SUIT12MODELPATH)
# data preprocess function
StandardScaler2 = pandas.read_pickle(SUIT2PREPROCESSPATH)
StandardScaler6 = pandas.read_pickle(SUIT6PREPROCESSPATH)
StandardScaler12 = pandas.read_pickle(SUIT12PREPROCESSPATH)

# size
# model
sizemodel0 = pandas.read_pickle(SIZEMODEL0PATH)
sizemodel1 = pandas.read_pickle(SIZEMODEL1PATH)
sizemodel2 = pandas.read_pickle(SIZEMODEL2PATH)
sizemodel3 = pandas.read_pickle(SIZEMODEL3PATH)
sizemodel = pandas.read_pickle(SIZEMODEL4PATH)
# data preprocess function
sizeStandardScaler0 = pandas.read_pickle(SIZESTANDARDSCALER0PATH)
sizeStandardScaler1 = pandas.read_pickle(SIZESTANDARDSCALER1PATH)
sizeStandardScaler2 = pandas.read_pickle(SIZESTANDARDSCALER2PATH)
sizeStandardScaler3 = pandas.read_pickle(SIZESTANDARDSCALER3PATH)

# compute
# suit compute

# suit2
def suit2(dataleft,dataright):
    left_data_preprocess2 =  StandardScaler2.transform([dataleft])
    right_data_preprocess2 = StandardScaler2.transform([dataright])
    predict_left = model2.predict_proba(left_data_preprocess2)
    predict_right = model2.predict_proba(right_data_preprocess2)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})
# suit6
def suit6(dataleft,dataright):
    left_data_preprocess6 =  StandardScaler6.transform([dataleft])
    right_data_preprocess6 = StandardScaler6.transform([dataright])
    predict_left = model6.predict_proba(left_data_preprocess6)
    predict_right = model6.predict_proba(right_data_preprocess6)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})
# suit12
def suit12(dataleft,dataright):
    left_data_preprocess12 =  StandardScaler12.transform([dataleft])
    right_data_preprocess12 = StandardScaler12.transform([dataright])
    predict_left = model12.predict_proba(left_data_preprocess12)
    predict_right = model12.predict_proba(right_data_preprocess12)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})

# size
def sizepredict(data):
    sizepreprocessdata0 = sizeStandardScaler0.transform([data])
    sizepreprocessdata1 = sizeStandardScaler1.transform([data])
    sizepreprocessdata2 = sizeStandardScaler2.transform([data])
    sizepreprocessdata3 = sizeStandardScaler3.transform([data])
    size_predict0 = sizemodel0.predict_proba(sizepreprocessdata0)[0][1]
    size_predict1 = sizemodel1.predict_proba(sizepreprocessdata1)[0][1]
    size_predict2 = sizemodel2.predict_proba(sizepreprocessdata2)[0][1]
    size_predict3 = sizemodel3.predict_proba(sizepreprocessdata3)[0][1]
    predictresult = sizemodel.predict_proba([[size_predict0,size_predict1,size_predict2,size_predict3]])
    return  json.dumps({'size':predictresult[0][1]})


if __name__ == "__main__":

    # etl 正常数据 uuid 存储队列
    redis_list_foot_last_etl = REDIS_LIST_FOOT_LAST_ETL
    # etl 正常数据 uuid foot_last 存储的哈希表
    redis_hashset_foot_last_etl = REDIS_HASHSET_FOOT_LAST_ETL
    # 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
    redis_list_compute_result = REDIS_LIST_COMPUTE_RESULT




    # redis instance
    my_rds = rds()
    # get data and compute
    count = 0
    while True:
        uuid = my_rds.blpop_data(redis_list_foot_last_etl)
        uuid = uuid.decode()
        logger.info('1.start receive data time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        logger.info(uuid)
        count += 1
        logger.info(str(count))
        foot_last_list = my_rds.SetGetHashData(redis_hashset_foot_last_etl,uuid)
        foot_last_list = foot_last_list.decode()
        foot_last_list = json.loads(foot_last_list)

        return_shop_no = None
        return_sex = None
        logger.info('2.get foot last dataetl data from redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

        if foot_last_list != None:

            # get data for model compute size and suit
            leftrightdatasalones = getetldataleftrightalone(foot_last_list)
            leftrightdatastogethers = getetldataleftrighttogether(foot_last_list)
            logger.info('3.get data in demand for model compute  time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                            time.localtime()))
            # save one uuid all result
            suit2resultlist = list()
            suit6resultlist = list()
            suit12resultlist = list()
            sizeresultlist = list()

            # suit compute
            for leftrightdatasalone in leftrightdatasalones:
                uuid = leftrightdatasalone[0]
                algoversion = leftrightdatasalone[1]
                shop_no = leftrightdatasalone[2]
                styleno = leftrightdatasalone[3]
                basicsize = leftrightdatasalone[4]
                sex = leftrightdatasalone[5]

                suit2result = suit2(leftrightdatasalone[6],leftrightdatasalone[7])
                suit6result = suit6(leftrightdatasalone[6], leftrightdatasalone[7])
                suit12result = suit12(leftrightdatasalone[6], leftrightdatasalone[7])

                key = uuid + "_" + algoversion + "_" + styleno + "_" + str(sex)

                suit2resultdict = dict()
                suit6resultdict = dict()
                suit12resultdict = dict()

                suit2resultdict["size"] = basicsize
                suit2resultdict["result"] = suit2result

                suit6resultdict["size"] = basicsize
                suit6resultdict["result"] = suit6result

                suit12resultdict["size"] = basicsize
                suit12resultdict["result"] = suit12result

                suit2resultlist.append([key, suit2resultdict])
                suit6resultlist.append([key, suit6resultdict])
                suit12resultlist.append([key, suit12resultdict])

            logger.info('4.suit model compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                 time.localtime()))

            # size model
            for leftrightdatastogether in leftrightdatastogethers:
                uuid = leftrightdatastogether[0]
                algoversion = leftrightdatastogether[1]
                shop_no = leftrightdatastogether[2]
                styleno = leftrightdatastogether[3]
                basicsize = leftrightdatastogether[4]
                sex = leftrightdatastogether[5]
                sizeresult = sizepredict(leftrightdatastogether[6])
                # for return
                return_shop_no = shop_no
                return_sex = str(sex)

                key = uuid + "_" + algoversion + "_" + styleno + "_" + str(sex)

                resultdict = dict()
                resultdict["size"] = basicsize
                resultdict["result"] = sizeresult
                sizeresultlist.append([key, resultdict])

            logger.info('5.size model compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                 time.localtime()))

            # result process dict(key:list(dict)})
            suit2resultprocess = resultdataprocess(suit2resultlist)
            suit6resultprocess = resultdataprocess(suit6resultlist)
            suit12resultprocess = resultdataprocess(suit12resultlist)
            sizeresultprocess  = resultdataprocess(sizeresultlist)
            logger.info('6.model compute result process time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                           time.localtime()))

            resultsave(suit2resultprocess,'suit_length_v1.0')
            resultsave(suit6resultprocess, 'suit_metatarsalegirth_v1.0')
            resultsave(suit12resultprocess, 'suit_global_v1.0')
            resultsave(sizeresultprocess, 'size_v1.0')

            logger.info('7.model compute result save time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                        time.localtime()))
            # return compute status
            return_data = {'shop_no': return_shop_no, 'uuid': uuid, 'sex': return_sex}
            return_data = json.dumps(return_data)
            my_rds.rpush_data(redis_list_compute_result,return_data)

            logger.info('8.model compute result send to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                              time.localtime()))




