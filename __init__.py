#!/usr/bin/env python

"""

地址   http://rabbitmq.mr-ping.com/
python3.5.2
docker pull rabbitmq

消息中间件：  1日志收集
            2大数据 归档 离线计算--mysql
            3实时数据处理  流计算

        异步处理   和主流业务无关的次要业务 比如 发邮件 短信

        应用接偶    卖商品  用户同时买商品 库存减少 很多人同时操作会产生很多请求导致服务器崩溃 中间可以用mq中间件异步持久处理
        流量消峰    商品秒杀   mq 过滤条件
java的操作
https://www.bilibili.com/video/BV1gW411H7Az?from=search&seid=17593354551793588648
"""
