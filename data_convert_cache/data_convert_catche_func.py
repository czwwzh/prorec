#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

# local
# from data_convert_cache.configuration import *
# from data_convert_cache.util_log import *

# online
from configuration import *
from util_log import *

logger = get_logger(LOG_FILE_PATH_FUNC, "func-log")

#  return  result
def sendtowx(returndata):
    logger.info(returndata)
    try:
        requests.post(RETURN_PORT_URL, data=returndata,timeout=1)
    except requests.ConnectionError as e:
        logger.info(str(e))
        logger.info("Send abnormal Connection Timeout.")
    except requests.ReadTimeout as e:
        logger.info(str(e))
        logger.info("Send abnormal Read Timeout")