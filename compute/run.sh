#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute1_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute2_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute3_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute4_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute5_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute6_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute7_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/wwwroot/py_ApiConter/log/modelcompute8_`date "+%Y-%m-%d"`.log 2>&1 &