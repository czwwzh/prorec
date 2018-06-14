from compute.util_redis import  Redis_db as rds
import time
# my_rds.SetGetHashData(REDIS_HASHSET_FOOT_LAST_ETL,"YB20180613211900sLT8QIXYuOSLzckR",'A,B')
if __name__ == '__main__':

    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    REDIS_HASHSET_SHOP_SEASON = 'redis_hashset_shop_season'
    # REDIS_HASHSET_FOOT_LAST_ETL = 'redis_hashset_footdata_etl'
    #
    my_rds = rds()
    # my_rds.dele(REDIS_HASHSET_FOOT_LAST_ETL)
    ss1 = my_rds.SetGetHashData("CA03MA").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss2 = my_rds.SetGetHashData("CA30BT").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss3 = my_rds.SetGetHashData("CA34BS").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss4 = my_rds.SetGetHashData("CA32BS").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss5 = my_rds.SetGetHashData("CA32BL").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss6 = my_rds.SetGetHashData("CA32BL").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss7 = my_rds.SetGetHashData("CA30BT").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss8 = my_rds.SetGetHashData("CA24BL").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss9 = my_rds.SetGetHashData("CA20TT").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss10 = my_rds.SetGetHashData("CA12BL").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss11 = my_rds.SetGetHashData("CA05MA").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ss12 = my_rds.SetGetHashData("CA03MA").decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))






