#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import time

# local
from data_convert_cache.configuration import *
from data_convert_cache.util_log import logger

# online
# from dataetl_configuration import *
# from util_log import logger

#  return  result
def sendtowx(returndata):
    logger.info('1.start send to port time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    logger.info(returndata)
    try:
        requests.post(RETURN_PORT_URL, data=returndata,timeout=1)
    except requests.ConnectionError as e:
        logger.info(str(e))
        logger.info("Send abnormal Connection Timeout.")
    except requests.ReadTimeout as e:
        logger.info(str(e))
        logger.info("Send abnormal Read Timeout")
    logger.info('2.return data finished time:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))