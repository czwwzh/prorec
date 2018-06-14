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
# from compute_etl_func import *
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
        # 从redis中读取etl之后的foot last数据
        uuid = my_rds.blpop_data(redis_list_foot_last_etl)
        uuid = uuid.decode()
        logger.info('1.start receive data time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        logger.info(uuid)
        count += 1
        logger.info(str(count))
        foot_last_list = my_rds.SetGetHashData(redis_hashset_foot_last_etl,uuid)
        foot_last_list = foot_last_list.decode()
        foot_last_list = json.loads(foot_last_list)

        # 返回数据定义
        return_flag = False
        return_shop_no = None
        return_sex = None
        logger.info('2.get foot last dataetl data from redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

        if foot_last_list != None:

            # get data for model compute size and suit
            left_right_datas_alones = get_etl_data_left_right_alone(foot_last_list)
            left_right_datas_togethers = get_etl_data_left_right_together(foot_last_list)
            logger.info('3.get data in demand for model compute  time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

            # 计算结果list定义
            # save one uuid all result
            suit2_result_list = list()
            suit6_result_list = list()
            suit12_result_list = list()
            size_result_list = list()

            # 舒适度模型计算
            # suit compute
            for leftrightdatasalone in left_right_datas_alones:
                uuid = leftrightdatasalone[0]
                algoversion = leftrightdatasalone[1]
                shop_no = leftrightdatasalone[2]
                shoelastbaseno = leftrightdatasalone[3]
                basicsize = leftrightdatasalone[4]
                sex = leftrightdatasalone[5]

                suit2result = suit2(leftrightdatasalone[6],leftrightdatasalone[7])
                suit6result = suit6(leftrightdatasalone[6], leftrightdatasalone[7])
                suit12result = suit12(leftrightdatasalone[6], leftrightdatasalone[7])

                key = uuid + "_" + algoversion + "_" + shoelastbaseno + "_" + str(sex)

                suit2_result_dict = dict()
                suit6_result_dict = dict()
                suit12_result_dict = dict()

                suit2_result_dict["size"] = basicsize
                suit2_result_dict["result"] = suit2result

                suit6_result_dict["size"] = basicsize
                suit6_result_dict["result"] = suit6result

                suit12_result_dict["size"] = basicsize
                suit12_result_dict["result"] = suit12result

                suit2_result_list.append([key, suit2_result_dict])
                suit6_result_list.append([key, suit6_result_dict])
                suit12_result_list.append([key, suit12_result_dict])

            logger.info('4.suit model compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                 time.localtime()))

            # size 模型计算
            # size model
            for leftrightdatastogether in left_right_datas_togethers:
                uuid = leftrightdatastogether[0]
                algoversion = leftrightdatastogether[1]
                shop_no = leftrightdatastogether[2]
                shoelastbaseno = leftrightdatastogether[3]
                basicsize = leftrightdatastogether[4]
                sex = leftrightdatastogether[5]
                sizeresult = sizepredict(leftrightdatastogether[6])

                # for return
                if return_flag == False:
                    return_shop_no = shop_no
                    return_sex = str(sex)
                    return_flag = True

                key = uuid + "_" + algoversion + "_" + shoelastbaseno + "_" + str(sex)

                resultdict = dict()
                resultdict["size"] = basicsize
                resultdict["result"] = sizeresult
                size_result_list.append([key, resultdict])

            logger.info('5.size model compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                 time.localtime()))

            # 模型计算结果处理
            # result process dict(key:list(dict)})
            suit2_result_process = result_data_process(suit2_result_list)
            suit6_result_process = result_data_process(suit6_result_list)
            suit12_result_process = result_data_process(suit12_result_list)
            size_result_process  = result_data_process(size_result_list)
            logger.info('6.model compute result process time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                           time.localtime()))

            # 模型计算结果存储
            # result_save(suit2_result_process, 'suit_length_v1.0')
            # result_save(suit6_result_process, 'suit_metatarsalegirth_v1.0')
            # result_save(suit12_result_process, 'suit_global_v1.0')
            # result_save(size_result_process, 'size_v1.0')
            # result_save([(suit2_result_process,'suit_length_v1.0')])
            result_save_batch([(suit2_result_process, 'suit_length_v1.0'),(suit6_result_process, 'suit_metatarsalegirth_v1.0'),(suit12_result_process, 'suit_global_v1.0'),(size_result_process, 'size_v1.0')])

            logger.info('7.model compute result save time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                        time.localtime()))
            # 返回数据的uuid shop_no sex 入redis
            # return compute status
            return_data = {'shop_no': return_shop_no, 'uuid': uuid, 'sex': return_sex}
            return_data = json.dumps(return_data)
            my_rds.rpush_data(redis_list_compute_result,return_data)

            logger.info('8.model compute result send to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                              time.localtime()))




