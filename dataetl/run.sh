#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup python -u /home/ec2-user/zhanghao/prodrec/dataetl/transfer.py >/dev/null 2>&1 &
nohup python -u /home/ec2-user/zhanghao/prodrec/dataetl/read.py >/dev/null 2>&1 &
