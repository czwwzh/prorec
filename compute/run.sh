#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute1_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute2_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute3_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute4_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute5_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute6_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute7_`date "+%Y-%m-%d"`.log 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py> /home/ec2-user/zhanghao/prodrec/compute/log/modelcompute8_`date "+%Y-%m-%d"`.log 2>&1 &