#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author: zhanghao
@contact: zhanghao@epoque.shoes
@file: test1.py
@time: 2018/5/29/029  13:42
"""
import json

import demjson


# main function
if __name__ == '__main__':
    data1 = '''{"measurementItemsNum": "74","customerInfoExt": "{"scanVersion": "v1.0", "algoVersion": "v1.0"}",
     "customerInfo": "{"customer_name":"","customer_age":0,"customer_sex":2,"customer_native_place":"","
     customer_height":0,"customer_phone_number":"","customer_email":"","customer_weixin":"","advice":{"
     abnormal_foot":0,"wear_socks":0,"end_flag":"0"},"customer_bid":"10008","algoVersion":"v1.0","scanVersion":"v1.0"}",
     "analysisReport": "{"LEFT_FOOT_TYPE":2,"LEFT_FOOT_INOUTSIDE_TURN":43,"LEFT_FOOT_INOUTSIDE_ROTATE":11,"
     RIGHT_FOOT_TYPE":2,"RIGHT_FOOT_INOUTSIDE_TURN":0,"RIGHT_FOOT_INOUTSIDE_ROTATE":28800}", "mesurementItemInfos": "{"
     foot_length_original": { "left":235.053, "right":235.29},"foot_length": { "left":235, "right":235},"
     first_metatarsophalangeal_convex_length": { "left":212, "right":212},"fifth_metatarsophalangeal_convex_length": { "
     left":183, "right":183},"first_metatarsophalangeal_joint_length": { "left":171, "right":171},"
     fifth_metatarsophalangeal_joint_length": { "left":149, "right":149},"tarsal_bone_length": { "left":130, "
     right":130},"waist_length": { "left":96, "right":96},"heel_heart_length": { "left":42, "right":42},"
     waist_girth_length": { "left":106, "right":106},"back_girth_length": { "left":81, "right":81},"
     metatarsophalangeal_length": { "left":198, "right":198},"heel_up_edge_distance": { "left":10.0376, "
     right":9.91606},"first_metatarsophalangeal_convex_width": { "left":40.9521, "right":37.7016},"
     fifth_metatarsophalangeal_convex_width": { "left":39.7814, "right":46.4833},"
     first_metatarsophalangeal_joint_width": { "left":45.581, "right":40.0163},"
     fifth_metatarsophalangeal_joint_width": { "left":44.8452, "right":50.4896},"base_width": { "left":90.4262, "
     right":90.506},"metatarsophalangeal_width": { "left":72.083, "right":75.8703},"waist_width": { "left":39.0984, "
     right":44.4829},"heel_heart_width": { "left":65.3565, "right":64.4381},"
     first_metatarsophalangeal_convex_footprint_width": { "left":40.1608, "right":36.7368},"
     fifth_metatarsophalangeal_convex_footprint_width": { "left":38.5162, "right":45.1751},"
     first_metatarsophalangeal_joint_footprint_width": { "left":42.2465, "right":35.4481},"
     fifth_metatarsophalangeal_joint_footprint_width": { "left":43.104, "right":48.7516},"waist_footprint_width": { "
     left":36.9727, "right":42.3587},"first_metatarsophalangeal_convex_edge_width": { "left":0.791298, "
     right":0.96479},"fifth_metatarsophalangeal_convex_edge_width": { "left":1.26522, "right":1.30818},"
     first_metatarsophalangeal_joint_edge_width": { "left":3.3345, "right":4.56822},"
     fifth_metatarsophalangeal_joint_edge_width": { "left":1.74122, "right":1.73806},"waist_edge_width": { "
     left":2.12565, "right":2.12417},"heel_heart_inside_edge_width": { "left":6.30887, "right":3.93455},"
     heel_heart_outside_edge_width": { "left":3.02502, "right":2.86806},"foot_arch_param": { "left":0.649088, "
     right":0.602948},"thumb_top_height": { "left":19.1497, "right":19.0102},"
     first_metatarsophalangeal_joint_height": { "left":35.8172, "right":36.9053},"tarsal_bone_height": { "
     left":43.8635, "right":47.6818},"lateral_malleolus_height": { "left":43.2893, "right":43.0834},"
     metatarsophalangeal_girth": { "left":161.613, "right":169.286},"plantar_girth": { "left":219.282, "
     right":222.032},"waist_girth": { "left":232.035, "right":234.387},"tarsal_girth": { "left":226.488, "
     right":227.729},"back_girth": { "left":235.473, "right":237.277},"pocket_heel_girth": { "left":289.398, "
     right":289.035},"ankle_girth": { "left":208.251, "right":211.757},"calf_height": { "left":0, "right":0},"
     below_knee_height": { "left":0, "right":0},"calf_girth": { "left":0, "right":0},"below_knee_girth": { "left":0, "
     right":0},"arch_top_height": { "left":0, "right":0},"arch_top_width": { "left":0, "right":0},"
     heel_inside_convex_length": { "left":0, "right":0},"heel_outside_convex_length": { "left":0, "right":0},"
     heel_convex_width": { "left":0, "right":0},"heel_inside_convex_width": { "left":0, "right":0},"
     heel_outside_convex_width": { "left":0, "right":0},"heel_gap": { "left":6.19571, "right":5.90956},"
     heel_gap_tolerance": { "left":3.09786, "right":2.95478},"heel_inside_convex_edge_width": { "left":0, "right":0},"
     heel_outside_convex_edge_width": { "left":0, "right":0},"boat_curve_height": { "left":59.7482, "right":65.6381},"
     ankle_height": { "left":96, "right":93},"kyphosis_height": { "left":14.3289, "right":16.0569},"
     back_arch_gap_54": { "left":7.61333, "right":7.90948},"back_arch_gap_70": { "left":9.90979, "right":9.70363},"
     back_arch_gap_85": { "left":10.2865, "right":10.4703},"back_arch_gap_90": { "left":10.3, "right":10.2847},"
     angle_between_heel_line_and_axis_line": { "left":0.281855, "right":4.02073},"foot_inoutside_turn": { "left":43, "
     right":0},"foot_inoutside_rotate": { "left":11, "right":28800},"first_metatarsophalangeal_length": { "
     left":234.998, "right":235.286},"second_metatarsophalangeal_length": { "left":225.3, "right":227.388},"
     third_metatarsophalangeal_length": { "left":209.557, "right":216.057},"shoe_type": { "left":0.5, "right":1}}",
     "UUID": "TX20180211154517gUcaeBEEwlWLQ8sK", "measurementItemExt": "{"scanVersion": "v1.0", "algoVersion": "v1.0"}",
     "scanDate": "2018-02-11 15:45:17", "customerId": "epoque", "scanId": "BL170528_02677", "algoVersion": "v1.0",
     "scanVersion": "v1.0"}'''
    data2 = '''{"measurementItemsNum":"74","customerInfoExt":"{"scanVersion": "v1.0", "algoVersion": "v1.0"}","customerInfo":"{"customer_name":"","customer_age":0,"customer_sex":2,"customer_native_place":"","customer_height":0,"customer_phone_number":"","customer_email":"","customer_weixin":"","advice":{"abnormal_foot":0,"wear_socks":0,"end_flag":"0"},"customer_bid":"10008","algoVersion":"v1.0","scanVersion":"v1.0"}","analysisReport":"{"LEFT_FOOT_TYPE":2,"LEFT_FOOT_INOUTSIDE_TURN":56,"LEFT_FOOT_INOUTSIDE_ROTATE":12,"RIGHT_FOOT_TYPE":2,"RIGHT_FOOT_INOUTSIDE_TURN":0,"RIGHT_FOOT_INOUTSIDE_ROTATE":28800}","mesurementItemInfos":"{"foot_length_original": { "left":244.021, "right":241.616},"foot_length": { "left":245, "right":240},"first_metatarsophalangeal_convex_length": { "left":221, "right":216},"fifth_metatarsophalangeal_convex_length": { "left":191, "right":187},"first_metatarsophalangeal_joint_length": { "left":178, "right":174},"fifth_metatarsophalangeal_joint_length": { "left":156, "right":152},"tarsal_bone_length": { "left":135, "right":133},"waist_length": { "left":100, "right":98},"heel_heart_length": { "left":44, "right":43},"waist_girth_length": { "left":111, "right":109},"back_girth_length": { "left":84, "right":82},"metatarsophalangeal_length": { "left":207, "right":202},"heel_up_edge_distance": { "left":11.7202, "right":11.6119},"first_metatarsophalangeal_convex_width": { "left":40.8345, "right":42.4728},"fifth_metatarsophalangeal_convex_width": { "left":48.4163, "right":49.7804},"first_metatarsophalangeal_joint_width": { "left":47.6311, "right":45.7298},"fifth_metatarsophalangeal_joint_width": { "left":50.9709, "right":51.7368},"base_width": { "left":98.602, "right":97.4667},"metatarsophalangeal_width": { "left":82.4515, "right":81.7718},"waist_width": { "left":37.0963, "right":37.8279},"heel_heart_width": { "left":66.6398, "right":63.6616},"first_metatarsophalangeal_convex_footprint_width": { "left":38.4166, "right":40.3678},"fifth_metatarsophalangeal_convex_footprint_width": { "left":46.9493, "right":48.7272},"first_metatarsophalangeal_joint_footprint_width": { "left":43.0026, "right":40.2504},"fifth_metatarsophalangeal_joint_footprint_width": { "left":49.7648, "right":50.5968},"waist_footprint_width": { "left":34.2451, "right":35.3782},"first_metatarsophalangeal_convex_edge_width": { "left":2.41788, "right":2.10498},"fifth_metatarsophalangeal_convex_edge_width": { "left":1.467, "right":1.05316},"first_metatarsophalangeal_joint_edge_width": { "left":4.62854, "right":5.47941},"fifth_metatarsophalangeal_joint_edge_width": { "left":1.20611, "right":1.13999},"waist_edge_width": { "left":2.85125, "right":2.44966},"heel_heart_inside_edge_width": { "left":6.14198, "right":5.19357},"heel_heart_outside_edge_width": { "left":3.09532, "right":3.18747},"foot_arch_param": { "left":0.416708, "right":0.434164},"thumb_top_height": { "left":19.3571, "right":21.1679},"first_metatarsophalangeal_joint_height": { "left":40.9556, "right":43.0116},"tarsal_bone_height": { "left":56.9962, "right":56.9519},"lateral_malleolus_height": { "left":46.2634, "right":46.7055},"metatarsophalangeal_girth": { "left":185.564, "right":188.952},"plantar_girth": { "left":241.86, "right":241.487},"waist_girth": { "left":245.523, "right":244.217},"tarsal_girth": { "left":240.4, "right":239.29},"back_girth": { "left":253.896, "right":251.55},"pocket_heel_girth": { "left":323.707, "right":317.77},"ankle_girth": { "left":220.658, "right":202.54},"calf_height": { "left":0, "right":0},"below_knee_height": { "left":0, "right":0},"calf_girth": { "left":0, "right":0},"below_knee_girth": { "left":0, "right":0},"arch_top_height": { "left":0, "right":0},"arch_top_width": { "left":0, "right":0},"heel_inside_convex_length": { "left":0, "right":0},"heel_outside_convex_length": { "left":0, "right":0},"heel_convex_width": { "left":0, "right":0},"heel_inside_convex_width": { "left":0, "right":0},"heel_outside_convex_width": { "left":0, "right":0},"heel_gap": { "left":8.11034, "right":7.73406},"heel_gap_tolerance": { "left":4.05517, "right":3.86703},"heel_inside_convex_edge_width": { "left":0, "right":0},"heel_outside_convex_edge_width": { "left":0, "right":0},"boat_curve_height": { "left":76.627, "right":72.7553},"ankle_height": { "left":105, "right":105},"kyphosis_height": { "left":19.2739, "right":20.9853},"back_arch_gap_54": { "left":9.53133, "right":8.30724},"back_arch_gap_70": { "left":11.7212, "right":11.3933},"back_arch_gap_85": { "left":13.2728, "right":13.4538},"back_arch_gap_90": { "left":13.7519, "right":13.8439},"angle_between_heel_line_and_axis_line": { "left":1.22637, "right":2.26304},"foot_inoutside_turn": { "left":56, "right":0},"foot_inoutside_rotate": { "left":12, "right":28800},"first_metatarsophalangeal_length": { "left":243.992, "right":240.145},"second_metatarsophalangeal_length": { "left":237.122, "right":232.853},"third_metatarsophalangeal_length": { "left":230.483, "right":223.752},"shoe_type": { "left":3, "right":3.5}}","UUID":"TX20180412195829yS3tbyxFfCuxzxTB","measurementItemExt":"{"scanVersion": "v1.0", "algoVersion": "v1.0"}","scanDate":"2018-04-12 19:58:29","customerId":"epoque","scanId":"BL160187_06579","algoVersion":"v1.0","scanVersion":"v1.0"}'''

    data = json.loads(data2.replace('''"{''', "{").replace('''}"''', "}").replace('''\\''', '').replace("b'","").replace("n'",""))
    # data = json.loads(data2)
    # data1 = json.loads(data1)
    print(data)


