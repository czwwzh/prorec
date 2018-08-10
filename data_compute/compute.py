#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy
import tensorflow


# local
# from data_compute.compute_func import *
# from data_compute.Log_Util import *
# from data_compute.Redis_Util import Redis_db as rds
# from data_compute.compute_configuration_test import *

tensorflow.enable_eager_execution()

# online
from compute_func import *
from Log_Util import *
from Redis_Util import Redis_db as rds
from compute_configuration_prod import *

# woman
# =============================================================================
# load model and function
# suit
# model
model2_woman = pandas.read_pickle(SUIT2_MODEL_PATH_WOMAN)
model6_woman = pandas.read_pickle(SUIT6_MODEL_PATH_WOMAN)
model12_woman = pandas.read_pickle(SUIT12_MODEL_PATH_WOMAN)
# data preprocess function
StandardScaler2_woman = pandas.read_pickle(SUIT2_PREPROCESS_PATH_WOMAN)
StandardScaler6_woman = pandas.read_pickle(SUIT6_PREPROCESS_PATH_WOMAN)
StandardScaler12_woman = pandas.read_pickle(SUIT12_PREPROCESS_PATH_WOMAN)

# size
# model
sizemodel0_woman = pandas.read_pickle(SIZE_MODEL0_PATH_WOMAN)
sizemodel1_woman = pandas.read_pickle(SIZE_MODEL1_PATH_WOMAN)
sizemodel2_woman = pandas.read_pickle(SIZE_MODEL2_PATH_WOMAN)
sizemodel3_woman = pandas.read_pickle(SIZE_MODEL3_PATH_WOMAN)
sizemodel_woman = pandas.read_pickle(SIZE_MODEL4_PATH_WOMAN)
# data preprocess function
sizeStandardScaler0_woman = pandas.read_pickle(SIZE_STANDARDSCALER0_PATH_WOMAN)
sizeStandardScaler1_woman = pandas.read_pickle(SIZE_STANDARDSCALER1_PATH_WOMAN)
sizeStandardScaler2_woman = pandas.read_pickle(SIZE_STANDARDSCALER2_PATH_WOMAN)
sizeStandardScaler3_woman = pandas.read_pickle(SIZE_STANDARDSCALER3_PATH_WOMAN)

# data_compute
# suit data_compute

# suit2
def suit2_woman(dataleft,dataright):
    left_data_preprocess2 =  StandardScaler2_woman.transform([dataleft])
    right_data_preprocess2 = StandardScaler2_woman.transform([dataright])
    predict_left = model2_woman.predict_proba(left_data_preprocess2)
    predict_right = model2_woman.predict_proba(right_data_preprocess2)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})
# suit6
def suit6_woman(dataleft,dataright):
    left_data_preprocess6 =  StandardScaler6_woman.transform([dataleft])
    right_data_preprocess6 = StandardScaler6_woman.transform([dataright])
    predict_left = model6_woman.predict_proba(left_data_preprocess6)
    predict_right = model6_woman.predict_proba(right_data_preprocess6)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})
# suit12
def suit12_woman(dataleft,dataright):
    left_data_preprocess12 =  StandardScaler12_woman.transform([dataleft])
    right_data_preprocess12 = StandardScaler12_woman.transform([dataright])
    predict_left = model12_woman.predict_proba(left_data_preprocess12)
    predict_right = model12_woman.predict_proba(right_data_preprocess12)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})

# size
def size_predict_woman(data):
    sizepreprocessdata0 = sizeStandardScaler0_woman.transform([data])
    sizepreprocessdata1 = sizeStandardScaler1_woman.transform([data])
    sizepreprocessdata2 = sizeStandardScaler2_woman.transform([data])
    sizepreprocessdata3 = sizeStandardScaler3_woman.transform([data])
    size_predict0 = sizemodel0_woman.predict_proba(sizepreprocessdata0)[0][1]
    size_predict1 = sizemodel1_woman.predict_proba(sizepreprocessdata1)[0][1]
    size_predict2 = sizemodel2_woman.predict_proba(sizepreprocessdata2)[0][1]
    size_predict3 = sizemodel3_woman.predict_proba(sizepreprocessdata3)[0][1]
    predictresult = sizemodel_woman.predict_proba([[size_predict0,size_predict1,size_predict2,size_predict3]])
    return  json.dumps({'size':predictresult[0][1]})


# man
# =============================================================================
# load model and function
# suit
# model
model2_man = pandas.read_pickle(SUIT2_MODEL_PATH_MAN)
model6_man = pandas.read_pickle(SUIT6_MODEL_PATH_MAN)
model12_man = pandas.read_pickle(SUIT12_MODEL_PATH_MAN)
# data preprocess function
StandardScaler2_man = pandas.read_pickle(SUIT2_PREPROCESS_PATH_MAN)
StandardScaler6_man = pandas.read_pickle(SUIT6_PREPROCESS_PATH_MAN)
StandardScaler12_man = pandas.read_pickle(SUIT12_PREPROCESS_PATH_MAN)


# compute
# suit compute
# suit2
def suit2_man(dataleft,dataright):
    left_data_preprocess2 =  StandardScaler2_man.transform([dataleft])
    right_data_preprocess2 = StandardScaler2_man.transform([dataright])
    predict_left = model2_man.predict_proba(left_data_preprocess2)
    predict_right = model2_man.predict_proba(right_data_preprocess2)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})
# suit6
def suit6_man(dataleft,dataright):
    left_data_preprocess6 =  StandardScaler6_man.transform([dataleft])
    right_data_preprocess6 = StandardScaler6_man.transform([dataright])
    predict_left = model6_man.predict_proba(left_data_preprocess6)
    predict_right = model6_man.predict_proba(right_data_preprocess6)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})
# suit12
def suit12_man(dataleft,dataright):
    left_data_preprocess12 =  StandardScaler12_man.transform([dataleft])
    right_data_preprocess12 = StandardScaler12_man.transform([dataright])
    predict_left = model12_man.predict_proba(left_data_preprocess12)
    predict_right = model12_man.predict_proba(right_data_preprocess12)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})

SizeStandardScaler0 = pandas.read_pickle(SIZE_StandardScaler_MLP_PATH0_MAN)
SizeStandardScaler1 = pandas.read_pickle(SIZE_StandardScaler_MLP_PATH1_MAN)
SizeStandardScaler2 = pandas.read_pickle(SIZE_StandardScaler_MLP_PATH2_MAN)

mlp_path0 = SIZE_MODEL_MLP_PATH0_MAN
mlp_path1 = SIZE_MODEL_MLP_PATH1_MAN
mlp_path2 = SIZE_MODEL_MLP_PATH2_MAN


lgbm0 = pandas.read_pickle(SIZE_MODEL_LGBM_PATH0_MAN)
lgbm1 = pandas.read_pickle(SIZE_MODEL_LGBM_PATH1_MAN)
lgbm2 = pandas.read_pickle(SIZE_MODEL_LGBM_PATH2_MAN)

lgbmStandardScaler0 = pandas.read_pickle(SIZE_StandardScaler_LGBM_PATH0_MAN)
lgbmStandardScaler1 = pandas.read_pickle(SIZE_StandardScaler_LGBM_PATH1_MAN)
lgbmStandardScaler2 = pandas.read_pickle(SIZE_StandardScaler_LGBM_PATH2_MAN)




w1_0 = tensorflow.get_variable('w1_0', [147, 147], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b1_0 = tensorflow.get_variable('b1_0', [147], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
w6_0 = tensorflow.get_variable('w6_0', [147, 2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b6_0 = tensorflow.get_variable('b6_0', [2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))

Saver0 = tensorflow.contrib.eager.Saver([w1_0, w6_0, b1_0, b6_0])
Saver0.restore(mlp_path0)


w1_1 = tensorflow.get_variable('w1_1', [147, 147], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b1_1 = tensorflow.get_variable('b1_1', [147], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
w6_1 = tensorflow.get_variable('w6_1', [147, 2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b6_1 = tensorflow.get_variable('b6_1', [2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))

Saver1 = tensorflow.contrib.eager.Saver([w1_1, w6_1, b1_1, b6_1])
Saver1.restore(mlp_path1)


w1_2 = tensorflow.get_variable('w1_2', [147, 147], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b1_2 = tensorflow.get_variable('b1_2', [147], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
w6_2 = tensorflow.get_variable('w6_2', [147, 2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b6_2 = tensorflow.get_variable('b6_2', [2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))

Saver2 = tensorflow.contrib.eager.Saver([w1_2, w6_2, b1_2, b6_2])
Saver2.restore(mlp_path2)


w1_stack = tensorflow.get_variable('w1_stack', [6, 32],
                                       initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b1_stack = tensorflow.get_variable('b1_stack', [32],
                                   initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
w6_stack = tensorflow.get_variable('w6_stack', [32, 2],
                                   initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
b6_stack = tensorflow.get_variable('b6_stack', [2], initializer=tensorflow.truncated_normal_initializer(stddev=0.1))
Saver = tensorflow.contrib.eager.Saver([w1_stack, w6_stack, b1_stack, b6_stack])
Saver.restore(SIZE_MODEL_STACK_MLP_PATH_MAN)

def size_predict_man(data):
    # global w1,b1,w6,b6,Saver
    k = []

    # mlp

    # 0
    temp_data0 = SizeStandardScaler0.transform(data).astype(numpy.float32)
    h1_0 = tensorflow.nn.relu(tensorflow.matmul(temp_data0, w1_0) + b1_0)
    h6_0 = tensorflow.matmul(h1_0, w6_0) + b6_0
    y=tensorflow.nn.softmax(h6_0).numpy()
    k.append(y[:,1].reshape(-1,1)[0])
    # 1
    temp_data1 = SizeStandardScaler1.transform(data).astype(numpy.float32)
    h1_1 = tensorflow.nn.relu(tensorflow.matmul(temp_data1, w1_1) + b1_1)
    h6_1 = tensorflow.matmul(h1_1, w6_1) + b6_1
    y = tensorflow.nn.softmax(h6_1).numpy()
    k.append(y[:, 1].reshape(-1, 1)[0])
    # 2
    temp_data2 = SizeStandardScaler2.transform(data).astype(numpy.float32)
    h1_2 = tensorflow.nn.relu(tensorflow.matmul(temp_data2, w1_2) + b1_2)
    h6_2 = tensorflow.matmul(h1_2, w6_2) + b6_2
    y = tensorflow.nn.softmax(h6_2).numpy()
    k.append(y[:, 1].reshape(-1, 1)[0])


    # lbgm

    # 0
    temp0 = lgbmStandardScaler0.transform(data)
    y = lgbm0.predict_proba(temp0)
    k.append(y[:, 1].reshape(-1, 1)[0])

    # 1
    temp1 = lgbmStandardScaler1.transform(data)
    y = lgbm1.predict_proba(temp1)
    k.append(y[:, 1].reshape(-1, 1)[0])

    # 2
    temp2 = lgbmStandardScaler2.transform(data)
    y = lgbm2.predict_proba(temp2)
    k.append(y[:, 1].reshape(-1, 1)[0])


    temp_data=numpy.array(k).reshape(-1,2*3).astype(numpy.float32)
    h1_stack = tensorflow.nn.relu(tensorflow.matmul(temp_data, w1_stack) + b1_stack)
    h6_stack = tensorflow.matmul(h1_stack, w6_stack) + b6_stack
    y=tensorflow.nn.softmax(h6_stack).numpy()

    result=json.dumps({'size':float(y[0][1])})

    return result


# 获取日志实例
logger = Logger("model-compute-log-3",LOG_FILE_PATH,1).getLogger()
if __name__ == "__main__":

    # etl 正常数据 uuid 存储队列
    redis_list_foot_etl = REDIS_LIST_FOOT_ETL

    # 模型计算完成数据shop_no  uuid  sex 进入的redis队列名称
    redis_list_compute_result = REDIS_LIST_COMPUTE_RESULT


    # redis instance
    my_rds = rds()

    # start data_compute
    count = 0
    try:
        while True:
            # 从redis中读取etl之后的foot数据
            foot_data = my_rds.blpop_data(redis_list_foot_etl)
            if foot_data != False and foot_data != None:
                logger.info('0. get footdata from redis time:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                count += 1
                logger.info(str(count))
                # 解析转换脚数据
                foot_data = foot_data.decode()
                foot_data = json.loads(foot_data)

                # 取出 shop_no customer_sex UUID
                shop_no = foot_data['shop_no']
                sex = foot_data['customer_sex']
                uuid = foot_data['UUID']
                logger.info(uuid)
                logger.info('1.data parase time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

                # foot connect last
                foot_last_list = foot_connect_last(foot_data)
                logger.info('2.foot connect last time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

                # 模型计算并返回
                # model data_compute
                if foot_last_list != None:

                    # get data for model data_compute size and suit
                    left_right_datas_alones = get_etl_data_left_right_alone(foot_last_list)
                    left_right_datas_togethers = get_etl_data_left_right_together(foot_last_list)
                    logger.info('3.get data in demand for model data_compute  time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

                    # 计算结果list定义
                    # save one uuid all result
                    suit2_result_list = list()
                    suit6_result_list = list()
                    suit12_result_list = list()
                    size_result_list = list()



                    # 舒适度模型计算
                    # suit data_compute
                    for leftrightdatasalone in left_right_datas_alones:
                        uuid = leftrightdatasalone[0]
                        algoversion = leftrightdatasalone[1]
                        shop_no = leftrightdatasalone[2]
                        shoelastbaseno = leftrightdatasalone[3]
                        basicsize = leftrightdatasalone[4]
                        sex = leftrightdatasalone[5]

                        if sex == 2:
                            suit2result = suit2_woman(leftrightdatasalone[6],leftrightdatasalone[7])
                            suit6result = suit6_woman(leftrightdatasalone[6], leftrightdatasalone[7])
                            suit12result = suit12_woman(leftrightdatasalone[6], leftrightdatasalone[7])
                        else:
                            suit2result = suit2_man(leftrightdatasalone[6], leftrightdatasalone[7])
                            suit6result = suit6_man(leftrightdatasalone[6], leftrightdatasalone[7])
                            suit12result = suit12_man(leftrightdatasalone[6], leftrightdatasalone[7])

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

                    logger.info('4.suit model data_compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
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
                        if sex == 2:
                            sizeresult = size_predict_woman(leftrightdatastogether[6])
                        else:
                            sizeresult = size_predict_man([leftrightdatastogether[6]])


                        key = uuid + "_" + algoversion + "_" + shoelastbaseno + "_" + str(sex)

                        resultdict = dict()
                        resultdict["size"] = basicsize
                        resultdict["result"] = sizeresult
                        size_result_list.append([key, resultdict])

                    logger.info('5.size model data_compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                         time.localtime()))

                    # 模型计算结果处理
                    # result process dict(key:list(dict)})
                    suit2_result_process = result_data_process(suit2_result_list)
                    suit6_result_process = result_data_process(suit6_result_list)
                    suit12_result_process = result_data_process(suit12_result_list)
                    size_result_process  = result_data_process(size_result_list)
                    logger.info('6.model data_compute result process time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                   time.localtime()))

                    # 模型计算结果存储
                    result_save_batch([(suit2_result_process, 'suit_length_v1.0'),(suit6_result_process, 'suit_metatarsalegirth_v1.0'),(suit12_result_process, 'suit_global_v1.0'),(size_result_process, 'size_v1.0')])

                    logger.info('7.model data_compute result save time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                time.localtime()))
                    # 返回数据的uuid shop_no sex 入redis
                    # return data_compute status
                    return_data = {'shop_no': shop_no, 'uuid': uuid, 'sex': str(sex)}
                    return_data = json.dumps(return_data)
                    my_rds.rpush_data(redis_list_compute_result,return_data)

                    logger.info('8.model data_compute result send to redis time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                      time.localtime()))

    except Exception as e:
        logger.info(str(e))




