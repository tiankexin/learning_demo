import sys
import pika

credentials = pika.PlainCredentials("tian", "tian")
conn = pika.ConnectionParameters("localhost",virtual_host='tian', credentials=credentials)

conn_broker = pika.BlockingConnection(conn)

channel=conn_broker.channel()

channel.exchange_declare(exchange="log_exchange",
                         exchange_type="direct",
                         durable=True,
                         auto_delete=False)
channel.queue_declare("error_log", durable=True)
channel.queue_declare("warning_log", durable=True)
channel.queue_declare("test_default", durable=True)
channel.queue_bind("error_log", "log_exchange", "error")
channel.queue_bind("warning_log", "log_exchange", "warning")

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

route_key = sys.argv[2]

channel.basic_publish(body=msg, exchange="log_exchange",
                      properties=msg_props,
                      routing_key=route_key)
