from model_test.configuration import *
from model_test.util_log import *

# 日志获取
logger = get_logger(LOG_FILE_PATH,"send-foot-data-log")

def get_foot_data(uuid_tuple):
    import pymysql

    db = None
    cursor = None


    sql = "select data from " + FOOT_SCAN_TABLE + " where uuid in" + str(uuid_tuple)


    result = None
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        result = cursor.fetchall()

    except Exception as e:
        logger.info(str(e))
        logger.info("save foot_scan exception")
    finally:
        if cursor != None:
            # 关闭游标
            cursor.close()
        if db != None:
            # 关闭数据库连接
            db.close()
    return result