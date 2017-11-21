import pika
import json
import time

credentials = pika.PlainCredentials("tian", "tian")
conn = pika.ConnectionParameters("localhost", virtual_host='tian', credentials=credentials)

conn_broker = pika.BlockingConnection(conn)

channel = conn_broker.channel()

msg = json.dumps({"client_name": "RPC Client 1.0",
                  "time": time.time()})

result_q = channel.queue_declare(exclusive=True, auto_delete=True)
msg_props = pika.BasicProperties()
msg_props.reply_to = result_q.method.queue
channel.basic_publish(body=msg,
                      exchange="rpc",
                      properties=msg_props,
                      routing_key="ping")
print "Sent 'ping' rpc call.Waiting for reply..."


def reply_callback(channel, method, header, body):
    print "RPC Reply---" + body
    channel.stop_consuming()


channel.basic_consume(reply_callback, queue=result_q.method.queue,
                      consumer_tag=result_q.method.queue)
channel.start_consuming()

