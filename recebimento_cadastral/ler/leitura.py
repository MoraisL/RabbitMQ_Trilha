import pika
import json
import os

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a fila para consumir os dados do RabbitMQ
channel.queue_declare(queue='dados_json')

# Diretório para salvar o arquivo único com todos os JSONs
output_directory = 'data'
os.makedirs(output_directory, exist_ok=True)

#Lino viniciius de makedirs(out)
# Caminho para o arquivo único de saída
output_file_path = os.path.join(output_directory, 'dados.json')
# Abre o arquivo em modo de adição ('a') para adicionar JSONs como linhas
output_file = open(output_file_path, 'a')

# Função para processar e salvar os dados recebidos como linhas em um único arquivo JSON
def receber_processar_e_salvar_json(ch, method, properties, body):
    # Decodifica a mensagem recebida
    data = json.loads(body)

    # Escreve o JSON como uma linha no arquivo
    output_file.write(json.dumps(data) + '\n')
    output_file.flush()  # Força a gravação imediata para o arquivo

    print(f"Dados recebidos e adicionados ao arquivo: {output_file_path}")

    # Confirmação de recebimento da mensagem
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configura o consumo da fila
channel.basic_consume(queue='dados_json', on_message_callback=receber_processar_e_salvar_json)
channel.basic_consume 
print('Aguardando dados do RabbitMQ...')
# Começa a consumir mensagens do RabbitMQ
try:
    channel.start_consuming()
except KeyboardInterrupt:
    # Fecha o arquivo ao interromper o programa
    output_file.close()
    print("Programa interrompido. Arquivo fechado.")
