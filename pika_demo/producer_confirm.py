import sys
import time
import pika
from pika import spec

print pika.__version__
credentials = pika.PlainCredentials("tian", "tian")
conn = pika.ConnectionParameters("localhost",virtual_host='tian', credentials=credentials)
conn_broker = pika.BlockingConnection(conn)
channel = conn_broker.channel()
msg_ids = []

channel.queue_declare("test_confirm")


def confirm_handler(frame):
    if type(frame.method) == spec.Confirm.SelectOk:
        print "Channel in 'confirm' mode."
    elif type(frame.method) == spec.Basic.Nack:
        if frame.method.delivery_tag in msg_ids:
            print "Message lost, id:{}".format(frame.method.delivery_tag)
    elif type(frame.method) == spec.Basic.Ack:
        if frame.method.delivery_tag in msg_ids:
            print "Confirm received!, id:{}".format(frame.method.delivery_tag)
            msg_ids.remove(frame.method.delivery_tag)

channel.confirm_delivery()
msg_list = ['aaaaa','bbbbb', 'cccccc', 'dddddd']
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'
begin_id = 0
for msg in msg_list:
    print channel.basic_publish(body=msg,
                          exchange="",
                          routing_key="test_confirm")
    msg_ids.append(begin_id +1)
    time.sleep(3)
channel.close()
