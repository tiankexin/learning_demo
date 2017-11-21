import pika
import json


credentials = pika.PlainCredentials("tian", "tian")
conn = pika.ConnectionParameters("localhost", virtual_host='tian', credentials=credentials)

conn_broker = pika.BlockingConnection(conn)
channel = conn_broker.channel()

channel.exchange_declare(exchange="rpc", exchange_type="direct", auto_delete=False)
channel.queue_declare(queue="ping", auto_delete=False)
channel.queue_bind("ping", exchange="rpc", routing_key="ping")


def api_ping(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    msg_dict = json.loads(body)
    print "Receive API call...replying..."
    channel.basic_publish(body="Pong!" + str(msg_dict["time"]),
                          exchange="",
                          routing_key=header.reply_to)
channel.basic_consume(api_ping, queue="ping",
                      consumer_tag="ping")
print "Waiting for RPC CALl..."
channel.start_consuming()
