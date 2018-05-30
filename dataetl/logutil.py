#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
import re
from logging.handlers import TimedRotatingFileHandler




# local
from dataetl.dataetlconfiguration import *
# online
# from dataetlconfiguration import *

logFilePath = logFilePath
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)


fh = TimedRotatingFileHandler(
    logFilePath,
    when="D",
    interval=1,
    backupCount=5)
# fh.suffix = "%Y-%m-%d_%H-%M-%S.log"
fh.suffix = "%Y-%m-%d.log"
fh.setLevel(logging.INFO)

# fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

