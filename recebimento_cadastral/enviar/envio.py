import pika
import json
import schedule
import time
import random
from datetime import datetime

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare uma fila para enviar dados para o RabbitMQ
channel.queue_declare(queue='dados_json')
# Função para enviar dados JSON psdffdhsghvinara o RabbitMQ
def enviar_dados():
    # Gerar um ID aleatório com 10 números
    _id = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    _cpf = ''.join([str(random.randint(0, 9)) for _ in range(11)])  # Corrigido para 11 dígitos  # Corrigido para 11 dígitos

    # Obter a data e hora atuais do sistema
    now = datetime.now()
    current_date = now.strftime('%d%m%Y')  # Formato AAAAMMDD
    current_time = now.strftime('%H%M%S')  # Formato HHMMSS
    # Montar os dados JSON com o ID aleatório e a data/hora atuais
    data = {
        "_id": _id,
        "cpf": _cpf,
        "date": current_date,
        "time": current_time,
        "customerCode": "Pefisa"
    }

    # Converter o dicionário em uma string JSON
    json_data = json.dumps(data)
    # Enviar os dados JSON para o RabbitMQ
    channel.basic_publish(exchange='', routing_key='dados_json', body=json_data)
    print(f"Dados enviados: {json_data}")

# Agendar o envio de dados a cada minuto
schedule.every(5).seconds.do(enviar_dados)

# Loop principal para executar o agendador
while True:
    schedule.run_pending()
    time.sleep(1)


while True:
    schedule.run_peding()
    time.sleep(1)
