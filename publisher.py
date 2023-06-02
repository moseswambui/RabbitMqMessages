import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')

for i in range(4):
    message = "Hello" + str(i)
    channel.basic_publish(exchange='br_exchange', routing_key='',body=message)

    print("[*] Sent %r" %message)

channel.exchange_delete(exchange='br_exchange', if_unused=False)
connection.close()