#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# durable=True
"""
使用工作队列的一个好处就是它能够并行的处理队列
如果一个工作者（worker）挂掉了，我们希望任务会重新发送给其他的工作者   no_ack=True 会关闭消息响应 去掉no_ack=Tru并设置ch.basic_ack(delivery_tag = method.delivery_tag)
当工作者（worker）挂掉这后，所有没有响应的消息都会重新发送。
排查不能够释放没相应的消息，那么rabbitmq会占据很多内存。
sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

消息持久化  分为队列持久化 消息持久化
队列持久化参数 durable=True 但是不允许存在相同的队列  消费者 生产者都要配置
消息持久化 在消费者配置 delivery_mode = 2
真正保证持久化，你需要改写你的代码来支持事务


为了不让其在同一时刻发送消息给同一个消费者 需要
channel.basic_qos(prefetch_count=1)
"""
channel.queue_declare(queue='task_queue', durable=True)
print (' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))
    time.sleep( str(body).count('.') )
    print (" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume('task_queue',callback,
                      )

channel.start_consuming()