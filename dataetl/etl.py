#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys,time,requests

# local
# from dataetl.etl_configuration import *
# from dataetl.util_redis import Redis_db as rds
# from dataetl.util_log import logger
# import dataetl.pp.pp as pp

# online
from etl_configuration import *
from util_redis import Redis_db as rds
from util_log import logger
import pp.pp as pp


ppservers = ()
if len(sys.argv) > 1:
    logger.info('Close Server')
    os._exit(0)
else:
    job_server = pp.Server(ppservers=ppservers)


def rundata(uuid):

    # online
    from readClass import readClass

    # local
    # from dataetl.readClass import readClass

    my_to = readClass()
    my_to.StartRun(uuid)

def AnaData(inputs,start_time):
    logger.info("deal with  " + str(len(inputs)) + " foot data")
    logger.info("deal with start time " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    jobs = [(input, job_server.submit(rundata, (input,), (), ())) for input in inputs]
    # logger.info(inputs)
    # logger.info(str(jobs))
    for input, job in jobs:
        # logger.info(input)
        # logger.info(job)
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
    while(True):
        # 从redis中读取数据
        res_tmp = my_rds.blpop_data(redis_kafka_list)
        logger.info(cpu_count)
        logger.info(res_tmp)
        start_time = time.time()
        if len(res_tmp)==32:
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

