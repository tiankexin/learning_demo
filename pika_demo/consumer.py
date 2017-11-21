import pika

credentials = pika.PlainCredentials("tian", "tian")
conn = pika.ConnectionParameters("localhost", virtual_host='tian', credentials=credentials)

conn_broker = pika.BlockingConnection(conn)

channel=conn_broker.channel()

channel.exchange_declare(exchange="hello-exchange",
                         exchange_type="direct",
                         durable=True,
                         auto_delete=False)

channel.queue_declare("hello-queue")
channel.queue_bind("hello-queue", exchange="hello-exchange", routing_key="hola")


def msg_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == "quit":
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print "receive msg >>>>>>>>>>>", body
    return

channel.basic_consume(msg_consumer, queue="hello-queue", consumer_tag="hello-consumer")
channel.queue_declare("hello-queue2")
channel.start_consuming()