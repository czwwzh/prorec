#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys,time,json
from redisutil import Redis_db as rds
import pp.pp as pp
import pandas

ppservers = ()
if len(sys.argv) > 1:
    print('Close Server')
    os._exit(0)
else:
    job_server = pp.Server(ppservers=ppservers)
# =============================================================================
# load model and function
# suit
# model
# model2 = pandas.read_pickle(SUIT2MODELPATH)
# model6 = pandas.read_pickle(SUIT6MODELPATH)
# model12 = pandas.read_pickle(SUIT12MODELPATH)
# # data preprocess function
# StandardScaler2 = pandas.read_pickle(SUIT2PREPROCESSPATH)
# StandardScaler6 = pandas.read_pickle(SUIT6PREPROCESSPATH)
# StandardScaler12 = pandas.read_pickle(SUIT12PREPROCESSPATH)
#
# # size
# # model
# sizemodel0 = pandas.read_pickle(SIZEMODEL0PATH)
# sizemodel1 = pandas.read_pickle(SIZEMODEL1PATH)
# sizemodel2 = pandas.read_pickle(SIZEMODEL2PATH)
# sizemodel3 = pandas.read_pickle(SIZEMODEL3PATH)
# sizemodel = pandas.read_pickle(SIZEMODEL4PATH)
# # data preprocess function
# sizeStandardScaler0 = pandas.read_pickle(SIZESTANDARDSCALER0PATH)
# sizeStandardScaler1 = pandas.read_pickle(SIZESTANDARDSCALER1PATH)
# sizeStandardScaler2 = pandas.read_pickle(SIZESTANDARDSCALER2PATH)
# sizeStandardScaler3 = pandas.read_pickle(SIZESTANDARDSCALER3PATH)

# compute
# suit compute

# suit2
def suit2(dataleft, dataright):
    model2 = pandas.read_pickle(SUIT2MODELPATH)
    # data preprocess function
    StandardScaler2 = pandas.read_pickle(SUIT2PREPROCESSPATH)

    left_data_preprocess2 = StandardScaler2.transform([dataleft])
    right_data_preprocess2 = StandardScaler2.transform([dataright])
    predict_left = model2.predict_proba(left_data_preprocess2)
    predict_right = model2.predict_proba(right_data_preprocess2)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})

# suit6
def suit6(dataleft, dataright):
    model6 = pandas.read_pickle(SUIT6MODELPATH)
    # data preprocess function
    StandardScaler6 = pandas.read_pickle(SUIT6PREPROCESSPATH)

    left_data_preprocess6 = StandardScaler6.transform([dataleft])
    right_data_preprocess6 = StandardScaler6.transform([dataright])
    predict_left = model6.predict_proba(left_data_preprocess6)
    predict_right = model6.predict_proba(right_data_preprocess6)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})

# suit12
def suit12(dataleft, dataright):
    model12 = pandas.read_pickle(SUIT12MODELPATH)
    # data preprocess function
    StandardScaler12 = pandas.read_pickle(SUIT12PREPROCESSPATH)
    left_data_preprocess12 = StandardScaler12.transform([dataleft])
    right_data_preprocess12 = StandardScaler12.transform([dataright])
    predict_left = model12.predict_proba(left_data_preprocess12)
    predict_right = model12.predict_proba(right_data_preprocess12)
    return json.dumps({'left': predict_left[0].tolist(), 'right': predict_right[0].tolist()})

# size
def sizepredict(data):
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


    sizepreprocessdata0 = sizeStandardScaler0.transform([data])
    sizepreprocessdata1 = sizeStandardScaler1.transform([data])
    sizepreprocessdata2 = sizeStandardScaler2.transform([data])
    sizepreprocessdata3 = sizeStandardScaler3.transform([data])
    size_predict0 = sizemodel0.predict_proba(sizepreprocessdata0)[0][1]
    size_predict1 = sizemodel1.predict_proba(sizepreprocessdata1)[0][1]
    size_predict2 = sizemodel2.predict_proba(sizepreprocessdata2)[0][1]
    size_predict3 = sizemodel3.predict_proba(sizepreprocessdata3)[0][1]
    predictresult = sizemodel.predict_proba([[size_predict0, size_predict1, size_predict2, size_predict3]])
    return json.dumps({'size': predictresult[0][1]})



def rundata(uuid):
    return_shop_no = None
    return_sex = None
    if uuid:
        print('1.data receive time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        status = statusexist(uuid)
        print("status:" + str(status))
        if status and status != 0:
            footlastlist = getetldata(uuid)
            print('2.get foot last dataetl data by uuid time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if footlastlist != None:
                # get data for model compute size and suit
                leftrightdatasalones = getetldataleftrightalone(footlastlist)
                leftrightdatastogethers = getetldataleftrighttogether(footlastlist)

                print('3.get  data in demand for model compute by uuid time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
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

                    suit2result = suit2(leftrightdatasalone[6], leftrightdatasalone[7])
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

                print('4.suit model compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
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
                print('5.size model compute time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                     time.localtime()))

                # result process dict(key:list(dict)})
                suit2resultprocess = resultdataprocess(suit2resultlist)
                suit6resultprocess = resultdataprocess(suit6resultlist)
                suit12resultprocess = resultdataprocess(suit12resultlist)
                sizeresultprocess = resultdataprocess(sizeresultlist)
                print('6.model compute result process time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                               time.localtime()))
                # # result save
                # dataset = [(suit2resultprocess, 'suit_length_v1.0'), (suit6resultprocess, 'suit_metatarsalegirth_v1.0'),
                #            (suit12resultprocess, 'suit_global_v1.0'), (sizeresultprocess, 'size_v1.0')]
                # agents = 4
                # with Pool(processes=agents) as pool:
                #     pool.map(resultsave, dataset)
                # result save
                resultsave(suit2resultprocess,'suit_length_v1.0')
                resultsave(suit6resultprocess, 'suit_metatarsalegirth_v1.0')
                resultsave(suit12resultprocess, 'suit_global_v1.0')
                resultsave(sizeresultprocess, 'size_v1.0')

                print('7.model compute result save time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                            time.localtime()))
                # return compute status
                returndata = {'shop_no': return_shop_no, 'uuid': uuid, 'sex': return_sex}
                print(returndata)
                a = requests.post(RETURN_PORT_URL, data=returndata)
                print(a)
                print('8.result send time:  ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                            time.localtime()))

def AnaData(inputs,start_time):
    print(len(inputs))
    jobs = [(input, job_server.submit(rundata, (input,), (suit2,suit6,suit12,sizepredict,), ('pandas','computeetlfunc',))) for input in inputs]
    for input, job in jobs:
        print('StartRun--->', input)
        res = job()
        print("------------------------------>",res )
        print('time:', time.time() - start_time)
    return  0



if __name__ == '__main__':
    cpu_count = int(job_server.get_ncpus())
    print("avaiable cpus ", cpu_count, "workers")
    my_rds = rds('recommend_data')
    start_time = time.time()
    rds_list = []
    while(True):
        res_tmp = my_rds.GetList()
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
