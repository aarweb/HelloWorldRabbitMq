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


def procesar(ch, method, properties, body):
    print(f"[📦] Pedido recibido: {body.decode()}")


channel.basic_consume(queue="pedidos", on_message_callback=procesar, auto_ack=True)
print("[*] Esperando pedidos. CTRL+C para salir")
channel.start_consuming()
