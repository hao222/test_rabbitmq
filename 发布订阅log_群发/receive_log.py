#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

# fanout 扇形交换机  把消息发送给它所知道的所有队列
"""
rabbitmqctl list_bindings  列出所有的绑定

exchange参数就是交换机的名称。空字符串代表默认或者匿名交换机：消息将会根据指定的routing_key分发到指定的队列。
服务器为我们选择一个随机的队列名  channel.queue_declare()
断开链接 队列应当立即删除 channel.queue_declare(exclusive=True)

queue_bind   创建绑定关系
"""

print (' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print (" [x] %r" % (body,))

channel.basic_consume(queue_name,callback,True)

channel.start_consuming()


