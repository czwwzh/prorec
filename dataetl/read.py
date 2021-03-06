#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys,time,requests

# local
import dataetl.pp.pp as pp
from dataetl.redisutil import Redis_db as rds

# online
# from redisutil import Redis_db as rds
# import pp.pp as pp



ppservers = ()
if len(sys.argv) > 1:
    print('Close Server')
    os._exit(0)
else:
    job_server = pp.Server(ppservers=ppservers)

def rundata(n):
    # local
    from dataetl.readClass import readClass
    # online
    # from readClass import readClass
    my_to = readClass()
    res = my_to.StartRun(n)

def AnaData(inputs,start_time):
    print(len(inputs),)
    jobs = [(input, job_server.submit(rundata, (input,), (), ())) for input in inputs]
    for input, job in jobs:
        res = job()
        print("------------------------------>",res )
        print('time:', time.time() - start_time)
    return  0

if __name__ == '__main__':
    cpu_count = int(job_server.get_ncpus())
    print("avaiable cpus ", cpu_count, "workers")
    my_rds = rds('recommend_data_msg')
    start_time = time.time()
    rds_list = []
    while(True):
        res_tmp = my_rds.GetList()
        print(res_tmp)
        start_time = time.time()
        if len(res_tmp)==32:
            res_tmp = res_tmp.decode()
        else:
            continue

        rds_list.append(res_tmp)
        list_count = len(rds_list)
        llen = my_rds.LenData()
        if list_count == cpu_count:
            print('********************************')
            list_count = AnaData(rds_list,start_time)

        if list_count > 0 and llen == 0:
            print('********************************---->')
            list_count = AnaData(rds_list,start_time)

        if list_count == 0 :
            rds_list = []

    # print "多线程下执行耗时: ", time.time() - start_time, "s"
    # job_server.print_stats()
