#!/bin/bash
source /home/ec2-user/virtualenv36/bin/activate
nohup python -u /home/ec2-user/zhanghao/prodrec/compute/modelcompute.py >/dev/null 2>&1 &