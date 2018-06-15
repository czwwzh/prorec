prodrec

v1.0.3

    data_compute   模型计算
         compute   模型计算入口  含模型
         compute_configuration  模型计算配置
         compute_func  模型计算数据处理函数
         util_log   日志工具脚本
         util_redis  redis连接、使用脚本
         variables   模型计算模块使用的变量定义
         run.sh  部署启动脚本
                 compute


    data_convert_catche 数据转换和处理脚本 辅助etl和compute
         configuration 配置文件
         data_convert_catche_func 函数定义
         kafka_redis kafka数据转redis队列脚本
         return_abnormal_data 异常脚数据发送接口脚本
         return_normal_data 模型计算完成发送接口脚本
         util_log 日志工具脚本
         util_redis redis连接、使用脚本
         run.sh  部署启动脚本
                 kafka_redis
                 return_abnormal_data
                 return_normal_data

    dataetl
         pp 多进程框架
         etl 多进程框架入口 脚数据etl入口
         etl_configuration 配置
         etl_func 函数定义
         readClass  数据etl过程类
         util_log   日志工具脚本
         util_redis  redis连接、使用脚本
         variables 脚数据etl所使用的变量
         run.sh  部署启动脚本
                 运行etl









