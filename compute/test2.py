from dataetl.data_etl_func import *
from dataetl.variables import *
# get foot and last data by uuid return list[dict]

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# spark python model redis hbase last


# sku recommend dataetl and compute table
RECOMMEND_DB_HOST = 'epoque-public.cwjobirlyklh.rds.cn-north-1.amazonaws.com.cn'
RECOMMEND_DB_PORT = 60916
RECOMMEND_DB_USER = "haozhShopRecom"
RECOMMEND_DB_PASSWORD = "zhanghaoShopSkuRecommand_38Yup9Bc5Ew7"
RECOMMEND_DB_NAME = 'shop_sku_recommend'
# RECOMMEND_DB_NAME = 'bdp_products'
RECOMMEND_DB_CHARSET = 'utf8mb4'
FOOT_LAST_ETL_TABLE = 'foot_last_etl'

#hbase configuration
# HBASE_HOST = '52.80.170.199'
HBASE_HOST = '54.222.249.145'
HBASE_TIMEOUT = 10000
HBASE_PORT = 9090
HBASE_PROTOCOL = 'compact'
HBASE_TRANSPORT = 'framed'
# prod
HBASE_EXCEPTION_TABLE = 'ShopSkuRecommends_RawException'
HBASE_RESULT_TABLE = 'ShopSkuRecommends_Result'

# test
# HBASE_EXCEPTION_TABLE = 'ShopSkuRecommends_RawExceptionTest'
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest'
# HBASE_RESULT_TABLE = 'ShopSkuRecommends_ResultTest3'

# model
SUIT2MODELPATH = '/suitmodel/lgbm_2'
SUIT6MODELPATH = '/suitmodel/lgbm_6'
SUIT12MODELPATH = '/suitmodel/lgbm_12'

# preprocess data
SUIT2PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_2'
SUIT6PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_6'
SUIT12PREPROCESSPATH = '/suitmodel/StandardScaler_lgbm_12'

# size model
# model
SIZEMODEL0PATH = '/sizemodel-2/lgbm_shoe_0'
SIZEMODEL1PATH = '/sizemodel-2/lgbm_shoe_1'
SIZEMODEL2PATH = '/sizemodel-2/lgbm_shoe_2'
SIZEMODEL3PATH = '/sizemodel-2/lgbm_shoe_3'
SIZEMODEL4PATH = '/sizemodel-2/stack_lgbm_shoe'
# data preprocess function
SIZESTANDARDSCALER0PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_0'
SIZESTANDARDSCALER1PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_1'
SIZESTANDARDSCALER2PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_2'
SIZESTANDARDSCALER3PATH = '/sizemodel-2/StandardScaler_lgbm_shoe_3'

# redis connection
# local
# REDIS_HOST = '192.168.17.110'
# prod
# REDIS_HOST = '54.222.236.85'
# REDIS_HOST = '52.80.83.193'
# REDIS_HOST = 'web-service-prod.rawr9u.ng.0001.cnn1.cache.amazonaws.com.cn'
# # REDIS_HOST = 'prod-sku-recommend.rawr9u.clustercfg.cnn1.cache.amazonaws.com.cn'
# REDIS_PORT = 6379
# REDIS_CONNECT_INFO = {'host':REDIS_HOST,'port':6379,'db':0}




# return url
# test
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# prod
RETURN_PORT_URL = 'http://epoque.epoque.cn/bdp/Bdsendmsg'
# RETURN_PORT_URL = 'http://test.epoque.cn/Testbigdata'
# compute completed return host
# RETURN_PORT_URL = 'http://54.222.142.37:9998/shopRecommendController/test'

logFilePath = '/home/ec2-user/zhanghao/log/computelog/modelcompute_v1.0'





FOOT_LAST_ORDER_DIMENSIONSSTR ='status,uuid,algoversion,shop_no,styleno,basicsize,sex,angle_between_heel_line_and_axis_line_left,angle_between_heel_line_and_axis_line_right,ankle_girth_left,ankle_girth_right,ankle_height_left,ankle_height_right,back_arch_gap_54_left,back_arch_gap_54_right,back_arch_gap_70_left,back_arch_gap_70_right,back_arch_gap_85_left,back_arch_gap_85_right,back_arch_gap_90_left,back_arch_gap_90_right,back_girth_left,back_girth_length_left,back_girth_length_right,back_girth_right,base_width_left,base_width_right,boat_curve_height_left,boat_curve_height_right,fattype,fifth_metatarsophalangeal_convex_edge_width_left,fifth_metatarsophalangeal_convex_edge_width_right,fifth_metatarsophalangeal_convex_footprint_width_left,fifth_metatarsophalangeal_convex_footprint_width_right,fifth_metatarsophalangeal_convex_length_left,fifth_metatarsophalangeal_convex_length_right,fifth_metatarsophalangeal_convex_width_left,fifth_metatarsophalangeal_convex_width_right,fifth_metatarsophalangeal_joint_edge_width_left,fifth_metatarsophalangeal_joint_edge_width_right,fifth_metatarsophalangeal_joint_footprint_width_left,fifth_metatarsophalangeal_joint_footprint_width_right,fifth_metatarsophalangeal_joint_length_left,fifth_metatarsophalangeal_joint_length_right,fifth_metatarsophalangeal_joint_width_left,fifth_metatarsophalangeal_joint_width_right,first_metatarsophalangeal_convex_edge_width_left,first_metatarsophalangeal_convex_edge_width_right,first_metatarsophalangeal_convex_footprint_width_left,first_metatarsophalangeal_convex_footprint_width_right,first_metatarsophalangeal_convex_length_left,first_metatarsophalangeal_convex_length_right,first_metatarsophalangeal_convex_width_left,first_metatarsophalangeal_convex_width_right,first_metatarsophalangeal_joint_edge_width_left,first_metatarsophalangeal_joint_edge_width_right,first_metatarsophalangeal_joint_footprint_width_left,first_metatarsophalangeal_joint_footprint_width_right,first_metatarsophalangeal_joint_height_left,first_metatarsophalangeal_joint_height_right,first_metatarsophalangeal_joint_length_left,first_metatarsophalangeal_joint_length_right,first_metatarsophalangeal_joint_width_left,first_metatarsophalangeal_joint_width_right,foot_arch_param_left,foot_arch_param_right,foot_length_left,foot_length_original_left,foot_length_original_right,foot_length_right,footaround,footbackarcdistance54mm,footbackarcdistancemouth,footbackbodylength,footbackfacedistance,footbackgirth,footbasicwidth,footbitfingeroutsidewidth,footboatcurveheight,footbottomheartconcavity,footdegreerejection,footfifthtoeoutsidewidth,footfirstplantarjointheight,footfirsttoeinsidewidth,footforepalmconvexity,footfrontcross,footheadthickness,footheelbulgeheight,footheelheartconvexity,footheelheartwidth,footheelheight,footlandspot,footmetatarsalgirth,footmouthbackheight,footmouthgirth,footmouthlength,footmouthwidth,footpalmwidth,footpocketheelgirth,footshoelastcalculatelength,foottarsalboneheight,foottarsalgirth,footthumbinsidewidth,footwaistgirth,footwaistwidth,footwidth,heel_gap_left,heel_gap_right,heel_gap_tolerance_left,heel_gap_tolerance_right,heel_heart_inside_edge_width_left,heel_heart_inside_edge_width_right,heel_heart_length_left,heel_heart_length_right,heel_heart_outside_edge_width_left,heel_heart_outside_edge_width_right,heel_heart_width_left,heel_heart_width_right,heel_up_edge_distance_left,heel_up_edge_distance_right,kyphosis_height_left,kyphosis_height_right,lateral_malleolus_height_left,lateral_malleolus_height_right,metatarsophalangeal_girth_left,metatarsophalangeal_girth_right,metatarsophalangeal_length_left,metatarsophalangeal_length_right,metatarsophalangeal_width_left,metatarsophalangeal_width_right,plantar_girth_left,plantar_girth_right,pocket_heel_girth_left,pocket_heel_girth_right,tarsal_bone_height_left,tarsal_bone_height_right,tarsal_bone_length_left,tarsal_bone_length_right,tarsal_girth_left,tarsal_girth_right,thumb_top_height_left,thumb_top_height_right,waist_edge_width_left,waist_edge_width_right,waist_footprint_width_left,waist_footprint_width_right,waist_girth_left,waist_girth_length_left,waist_girth_length_right,waist_girth_right,waist_length_left,waist_length_right,waist_width_left,waist_width_right'
FOOT_LAST_ORDER_DIMENSIONSSTR_VALUES = '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


FOOT_LAST_ORDER_LEFT_DIMENSIONSSTR ='foot_length_original_left,foot_length_left,first_metatarsophalangeal_convex_length_left,fifth_metatarsophalangeal_convex_length_left,first_metatarsophalangeal_joint_length_left,fifth_metatarsophalangeal_joint_length_left,tarsal_bone_length_left,waist_length_left,heel_heart_length_left,waist_girth_length_left,back_girth_length_left,metatarsophalangeal_length_left,heel_up_edge_distance_left,first_metatarsophalangeal_convex_width_left,fifth_metatarsophalangeal_convex_width_left,first_metatarsophalangeal_joint_width_left,fifth_metatarsophalangeal_joint_width_left,base_width_left,metatarsophalangeal_width_left,waist_width_left,heel_heart_width_left,first_metatarsophalangeal_convex_footprint_width_left,fifth_metatarsophalangeal_convex_footprint_width_left,first_metatarsophalangeal_joint_footprint_width_left,fifth_metatarsophalangeal_joint_footprint_width_left,waist_footprint_width_left,first_metatarsophalangeal_convex_edge_width_left,fifth_metatarsophalangeal_convex_edge_width_left,first_metatarsophalangeal_joint_edge_width_left,fifth_metatarsophalangeal_joint_edge_width_left,waist_edge_width_left,heel_heart_inside_edge_width_left,heel_heart_outside_edge_width_left,foot_arch_param_left,thumb_top_height_left,first_metatarsophalangeal_joint_height_left,tarsal_bone_height_left,lateral_malleolus_height_left,metatarsophalangeal_girth_left,plantar_girth_left,waist_girth_left,tarsal_girth_left,back_girth_left,pocket_heel_girth_left,ankle_girth_left,heel_gap_left,heel_gap_tolerance_left,boat_curve_height_left,ankle_height_left,kyphosis_height_left,back_arch_gap_54_left,back_arch_gap_70_left,back_arch_gap_85_left,back_arch_gap_90_left,angle_between_heel_line_and_axis_line_left,fattype,footaround,footbackarcdistance54mm,footbackarcdistancemouth,footbackbodylength,footbackfacedistance,footbackgirth,footbasicwidth,footbitfingeroutsidewidth,footboatcurveheight,footbottomheartconcavity,footdegreerejection,footfifthtoeoutsidewidth,footfirstplantarjointheight,footfirsttoeinsidewidth,footforepalmconvexity,footfrontcross,footheadthickness,footheelbulgeheight,footheelheartconvexity,footheelheartwidth,footheelheight,footlandspot,footmetatarsalgirth,footmouthbackheight,footmouthgirth,footmouthlength,footmouthwidth,footpalmwidth,footpocketheelgirth,footshoelastcalculatelength,foottarsalboneheight,foottarsalgirth,footthumbinsidewidth,footwaistgirth,footwaistwidth,footwidth'
FOOT_LAST_ORDER_RIGHT_DIMENSIONSSTR = 'foot_length_original_right,foot_length_right,first_metatarsophalangeal_convex_length_right,fifth_metatarsophalangeal_convex_length_right,first_metatarsophalangeal_joint_length_right,fifth_metatarsophalangeal_joint_length_right,tarsal_bone_length_right,waist_length_right,heel_heart_length_right,waist_girth_length_right,back_girth_length_right,metatarsophalangeal_length_right,heel_up_edge_distance_right,first_metatarsophalangeal_convex_width_right,fifth_metatarsophalangeal_convex_width_right,first_metatarsophalangeal_joint_width_right,fifth_metatarsophalangeal_joint_width_right,base_width_right,metatarsophalangeal_width_right,waist_width_right,heel_heart_width_right,first_metatarsophalangeal_convex_footprint_width_right,fifth_metatarsophalangeal_convex_footprint_width_right,first_metatarsophalangeal_joint_footprint_width_right,fifth_metatarsophalangeal_joint_footprint_width_right,waist_footprint_width_right,first_metatarsophalangeal_convex_edge_width_right,fifth_metatarsophalangeal_convex_edge_width_right,first_metatarsophalangeal_joint_edge_width_right,fifth_metatarsophalangeal_joint_edge_width_right,waist_edge_width_right,heel_heart_inside_edge_width_right,heel_heart_outside_edge_width_right,foot_arch_param_right,thumb_top_height_right,first_metatarsophalangeal_joint_height_right,tarsal_bone_height_right,lateral_malleolus_height_right,metatarsophalangeal_girth_right,plantar_girth_right,waist_girth_right,tarsal_girth_right,back_girth_right,pocket_heel_girth_right,ankle_girth_right,heel_gap_right,heel_gap_tolerance_right,boat_curve_height_right,ankle_height_right,kyphosis_height_right,back_arch_gap_54_right,back_arch_gap_70_right,back_arch_gap_85_right,back_arch_gap_90_right,angle_between_heel_line_and_axis_line_right,fattype,footaround,footbackarcdistance54mm,footbackarcdistancemouth,footbackbodylength,footbackfacedistance,footbackgirth,footbasicwidth,footbitfingeroutsidewidth,footboatcurveheight,footbottomheartconcavity,footdegreerejection,footfifthtoeoutsidewidth,footfirstplantarjointheight,footfirsttoeinsidewidth,footforepalmconvexity,footfrontcross,footheadthickness,footheelbulgeheight,footheelheartconvexity,footheelheartwidth,footheelheight,footlandspot,footmetatarsalgirth,footmouthbackheight,footmouthgirth,footmouthlength,footmouthwidth,footpalmwidth,footpocketheelgirth,footshoelastcalculatelength,foottarsalboneheight,foottarsalgirth,footthumbinsidewidth,footwaistgirth,footwaistwidth,footwidth'


FOOT_LAST_ORDER_DIMENSIONS =   ['angle_between_heel_line_and_axis_line_left',
                    'angle_between_heel_line_and_axis_line_right',
                    'ankle_girth_left',
                    'ankle_girth_right',
                    'ankle_height_left',
                    'ankle_height_right',
                    'back_arch_gap_54_left',
                    'back_arch_gap_54_right',
                    'back_arch_gap_70_left',
                    'back_arch_gap_70_right',
                    'back_arch_gap_85_left',
                    'back_arch_gap_85_right',
                    'back_arch_gap_90_left',
                    'back_arch_gap_90_right',
                    'back_girth_left',
                    'back_girth_length_left',
                    'back_girth_length_right',
                    'back_girth_right',
                    'base_width_left',
                    'base_width_right',
                    'boat_curve_height_left',
                    'boat_curve_height_right',
                    'fattype',
                    'fifth_metatarsophalangeal_convex_edge_width_left',
                    'fifth_metatarsophalangeal_convex_edge_width_right',
                    'fifth_metatarsophalangeal_convex_footprint_width_left',
                    'fifth_metatarsophalangeal_convex_footprint_width_right',
                    'fifth_metatarsophalangeal_convex_length_left',
                    'fifth_metatarsophalangeal_convex_length_right',
                    'fifth_metatarsophalangeal_convex_width_left',
                    'fifth_metatarsophalangeal_convex_width_right',
                    'fifth_metatarsophalangeal_joint_edge_width_left',
                    'fifth_metatarsophalangeal_joint_edge_width_right',
                    'fifth_metatarsophalangeal_joint_footprint_width_left',
                    'fifth_metatarsophalangeal_joint_footprint_width_right',
                    'fifth_metatarsophalangeal_joint_length_left',
                    'fifth_metatarsophalangeal_joint_length_right',
                    'fifth_metatarsophalangeal_joint_width_left',
                    'fifth_metatarsophalangeal_joint_width_right',
                    'first_metatarsophalangeal_convex_edge_width_left',
                    'first_metatarsophalangeal_convex_edge_width_right',
                    'first_metatarsophalangeal_convex_footprint_width_left',
                    'first_metatarsophalangeal_convex_footprint_width_right',
                    'first_metatarsophalangeal_convex_length_left',
                    'first_metatarsophalangeal_convex_length_right',
                    'first_metatarsophalangeal_convex_width_left',
                    'first_metatarsophalangeal_convex_width_right',
                    'first_metatarsophalangeal_joint_edge_width_left',
                    'first_metatarsophalangeal_joint_edge_width_right',
                    'first_metatarsophalangeal_joint_footprint_width_left',
                    'first_metatarsophalangeal_joint_footprint_width_right',
                    'first_metatarsophalangeal_joint_height_left',
                    'first_metatarsophalangeal_joint_height_right',
                    'first_metatarsophalangeal_joint_length_left',
                    'first_metatarsophalangeal_joint_length_right',
                    'first_metatarsophalangeal_joint_width_left',
                    'first_metatarsophalangeal_joint_width_right',
                    'foot_arch_param_left',
                    'foot_arch_param_right',
                    'foot_length_left',
                    'foot_length_original_left',
                    'foot_length_original_right',
                    'foot_length_right',
                    'footaround',
                    'footbackarcdistance54mm',
                    'footbackarcdistancemouth',
                    'footbackbodylength',
                    'footbackfacedistance',
                    'footbackgirth',
                    'footbasicwidth',
                    'footbitfingeroutsidewidth',
                    'footboatcurveheight',
                    'footbottomheartconcavity',
                    'footdegreerejection',
                    'footfifthtoeoutsidewidth',
                    'footfirstplantarjointheight',
                    'footfirsttoeinsidewidth',
                    'footforepalmconvexity',
                    'footfrontcross',
                    'footheadthickness',
                    'footheelbulgeheight',
                    'footheelheartconvexity',
                    'footheelheartwidth',
                    'footheelheight',
                    'footlandspot',
                    'footmetatarsalgirth',
                    'footmouthbackheight',
                    'footmouthgirth',
                    'footmouthlength',
                    'footmouthwidth',
                    'footpalmwidth',
                    'footpocketheelgirth',
                    'footshoelastcalculatelength',
                    'foottarsalboneheight',
                    'foottarsalgirth',
                    'footthumbinsidewidth',
                    'footwaistgirth',
                    'footwaistwidth',
                    'footwidth',
                    'heel_gap_left',
                    'heel_gap_right',
                    'heel_gap_tolerance_left',
                    'heel_gap_tolerance_right',
                    'heel_heart_inside_edge_width_left',
                    'heel_heart_inside_edge_width_right',
                    'heel_heart_length_left',
                    'heel_heart_length_right',
                    'heel_heart_outside_edge_width_left',
                    'heel_heart_outside_edge_width_right',
                    'heel_heart_width_left',
                    'heel_heart_width_right',
                    'heel_up_edge_distance_left',
                    'heel_up_edge_distance_right',
                    'kyphosis_height_left',
                    'kyphosis_height_right',
                    'lateral_malleolus_height_left',
                    'lateral_malleolus_height_right',
                    'metatarsophalangeal_girth_left',
                    'metatarsophalangeal_girth_right',
                    'metatarsophalangeal_length_left',
                    'metatarsophalangeal_length_right',
                    'metatarsophalangeal_width_left',
                    'metatarsophalangeal_width_right',
                    'plantar_girth_left',
                    'plantar_girth_right',
                    'pocket_heel_girth_left',
                    'pocket_heel_girth_right',
                    'tarsal_bone_height_left',
                    'tarsal_bone_height_right',
                    'tarsal_bone_length_left',
                    'tarsal_bone_length_right',
                    'tarsal_girth_left',
                    'tarsal_girth_right',
                    'thumb_top_height_left',
                    'thumb_top_height_right',
                    'waist_edge_width_left',
                    'waist_edge_width_right',
                    'waist_footprint_width_left',
                    'waist_footprint_width_right',
                    'waist_girth_left',
                    'waist_girth_length_left',
                    'waist_girth_length_right',
                    'waist_girth_right',
                    'waist_length_left',
                    'waist_length_right',
                    'waist_width_left',
                    'waist_width_right']



def getetldata(uuid):
    footlastlist = list()
    sql = "SELECT " + FOOT_LAST_ORDER_DIMENSIONSSTR + " FROM " + FOOT_LAST_ETL_TABLE + " where uuid = '" + uuid + "'"
    db = None
    try:
        db = pymysql.connect(host=RECOMMEND_DB_HOST, port=RECOMMEND_DB_PORT,
                             user=RECOMMEND_DB_USER, password=RECOMMEND_DB_PASSWORD,
                             db=RECOMMEND_DB_NAME, charset=RECOMMEND_DB_CHARSET)
        cursor = db.cursor()
        ist = cursor.execute(sql)
        if ist == 0 or ist == None:
            # updateexceptioncode(uuid,-4)
            return None
        results = cursor.fetchall()
        for result in results:
            footlast = getFootLastData(result)
            footlastlist.append(footlast)
    except:
        # print("Error:fecth foot and last data exception by uuid")
        logger.info("Error:fecth foot and last data exception by uuid")
    finally:
        if db:
            db.close()
    return footlastlist

# get one foot and last return a dict
def getFootLastData(data):
    footlastdata = dict()
    index = 7
    for field in FOOT_LAST_ORDER_DIMENSIONS:
        footlastdata[field] = data[index]
        index = index + 1

    footlastdata['uuid'] = data[1],
    if type(footlastdata['uuid']) == tuple:
        footlastdata['uuid'] = footlastdata['uuid'][0]

    footlastdata['algoversion'] = data[2],
    if type(footlastdata['algoversion']) == tuple:
        footlastdata['algoversion'] = footlastdata['algoversion'][0]

    footlastdata['shop_no'] = data[3],
    if type(footlastdata['shop_no']) == tuple:
        footlastdata['shop_no'] = footlastdata['shop_no'][0]

    footlastdata['styleno'] =  data[4],
    if type(footlastdata['styleno']) == tuple:
        footlastdata['styleno'] = footlastdata['styleno'][0]

    footlastdata['basicsize'] = data[5]
    footlastdata['sex'] = data[6]

    return footlastdata

if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20170612090630CB1rZWIIDus8xMO2')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180206164247atsZub6gqeuUU3XT')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20170612090630CB1rZWIIDus8xMO2')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180206164247atsZub6gqeuUU3XT')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180207142158MxIGpbFBS60eua0d')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210065400IPVIOgywrGBHUkSt')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210065400IPVIOgywrGBHUkSt')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210065537D4UvNiVPUMZSItxV')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210112541oSNMskXGJPGOwapW')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210140326I9Clx29LjWRRQALx')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20170612090630CB1rZWIIDus8xMO2')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180206164247atsZub6gqeuUU3XT')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20170612090630CB1rZWIIDus8xMO2')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180206164247atsZub6gqeuUU3XT')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180207142158MxIGpbFBS60eua0d')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210065400IPVIOgywrGBHUkSt')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210065400IPVIOgywrGBHUkSt')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210065537D4UvNiVPUMZSItxV')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210112541oSNMskXGJPGOwapW')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    getetldata('TX20180210140326I9Clx29LjWRRQALx')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



