#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys,time

# local
# from dataetl.etl_configuration_test import *
# from dataetl.Redis_Util import Redis_db as rds
# from dataetl.Log_Util import Logger
# import dataetl.pp.pp as pp

# online
from etl_configuration_prod import *
from Redis_Util import Redis_db as rds
from Log_Util import Logger
import pp.pp as pp

# 获取日志实例
logger = Logger("data-etl-log-4",LOG_FILE_PATH,0).getLogger()

ppservers = ()
if len(sys.argv) > 1:
    logger.info('Close Server')
    os._exit(0)
else:
    job_server = pp.Server(ppservers=ppservers)


def rundata(uuid):



    # local
    # from dataetl.readClass import readClass

    # online
    from readClass import readClass

    my_to = readClass()
    my_to.StartRun(uuid)

def AnaData(inputs,start_time):
    logger.info("deal with  " + str(len(inputs)) + " foot data")
    logger.info("deal with start time " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    jobs = [(input, job_server.submit(rundata, (input,), (), ())) for input in inputs]
    for input, job in jobs:
        job()
        # logger.info("----------------->" + str(res))
    logger.info("deal with end time " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    logger.info('time:' + str(time.time() - start_time))
    return  0


if __name__ == '__main__':
    cpu_count = int(job_server.get_ncpus())
    logger.info("avaiable cpus " + str(cpu_count))

    # redis 初始化
    my_rds = rds()
    redis_kafka_list = REDIS_KAFKA_LIST
    start_time = time.time()

    # list定义（从redis中读取数据放入list中）
    rds_list = list()

    try:
        while(True):
            # 从redis中读取数据
            res_tmp = my_rds.blpop_data(redis_kafka_list)
            start_time = time.time()
            if res_tmp != None and res_tmp!= False:
                res_tmp = res_tmp.decode()
            else:
                continue

            # 合法数据入list
            rds_list.append(res_tmp)

            # 实时比对 redis队列的长度 和这里定义的数组长度启动etl计算
            list_count = len(rds_list)
            llen = my_rds.len_redis_list(redis_kafka_list)

            if list_count == cpu_count:
                logger.info('***********start data  etl*************')
                list_count = AnaData(rds_list,start_time)

            if list_count > 0 and llen == 0:
                logger.info('***********start data  etl*************')
                list_count = AnaData(rds_list,start_time)

            if list_count == 0 :
                rds_list = list()
    except Exception as e:
        logger.info(str(e))

