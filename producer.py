import os

import pika

rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
rabbitmq_user = os.getenv("RABBITMQ_USER", "guest")
rabbitmq_pass = os.getenv("RABBITMQ_PASS", "guest")

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_host, credentials=credentials)
)
channel = connection.channel()

channel.queue_declare(queue="pedidos")

channel.basic_publish(
    exchange="",  # Default exchange
    routing_key="pedidos",  # = nombre de la cola
    body="Pedido #001: 2x Laptop, 1x Ratón",
)

print("[✓] Pedido enviado")
connection.close()
