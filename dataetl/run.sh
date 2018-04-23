#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/dataetl/transfer.py> /home/ec2-user/zhanghao/prodrec/dataetl/log/transfer_`date "+%Y-%m-%d"`.log 2>&1 &
nohup /usr/bin/python3.6 -u /home/ec2-user/zhanghao/prodrec/dataetl/read.py> /home/ec2-user/zhanghao/prodrec/dataetl/log/read_`date "+%Y-%m-%d"`.log 2>&1 &