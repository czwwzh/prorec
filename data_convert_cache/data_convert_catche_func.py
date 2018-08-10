#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

# local
# from data_convert_cache.configuration_test import *
# from data_convert_cache.Log_Util import Logger

# online
from configuration_prod import *
from Log_Util import Logger

# 获取日志实例
logger = Logger("func-log",LOG_FILE_PATH_FUNC,1).getLogger()

#  return  result
def sendtowx(returndata):
    logger.info(returndata)
    try:
        requests.post(RETURN_PORT_URL, data=returndata,timeout=1)
    except requests.ConnectionError as e:
        logger.error(str(e))
        logger.info("Send abnormal Connection Timeout.")
    except requests.ReadTimeout as e:
        logger.info(str(e))
        logger.info("Send abnormal Read Timeout")