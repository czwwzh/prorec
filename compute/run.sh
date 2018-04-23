#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute1_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute2_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute3_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute4_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute5_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute6_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute7_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/modelcompute8_`date "+%Y-%m-%d"`.log 2>&1 &