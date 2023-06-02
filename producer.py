import pika

# If you want to have a more secure SSL authentication, use ExternalCredentials object instead
credentials = pika.PlainCredentials(username='moses', password='12345', erase_on_connect=True)
parameters = pika.ConnectionParameters(host='127.0.0.1', port=5672, virtual_host='debt_manage', credentials=credentials)

# We are using BlockingConnection adapter to start a session. It uses a procedural approach to using Pika and has most of the asynchronous expectations removed
connection = pika.BlockingConnection(parameters)
# A channel provides a wrapper for interacting with RabbitMQ
channel = connection.channel()

# Check for a queue and create it, if necessary
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print("Subscriber queue_name", queue_name)
# For the sake of simplicity, we are not declaring an exchange, so the subsequent publish call will be sent to a Default exchange that is predeclared by the broker
channel.basic_publish(exchange='br_exchange', routing_key='hello', body='Checking Consumer availability!')
print(" [x] Sent 'Hello World!'")

# Safely disconnect from RabbitMQ
connection.close()  