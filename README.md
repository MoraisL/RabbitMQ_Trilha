Trilha de Conhecimento: RabbitMQ

Objetivo:

Este guia visa fornecer uma introdução completa ao RabbitMQ, explicando o que é, como instalá-lo, utilizá-lo e exemplos de usos comuns.
O que é RabbitMQ?

RabbitMQ é um message broker de código aberto que implementa o Advanced Message Queuing Protocol (AMQP). Ele facilita a comunicação entre diferentes partes de um sistema distribuído, permitindo que as mensagens sejam enviadas e recebidas de forma assíncrona.
Instalação do RabbitMQ

    Pré-requisitos:
        Erlang/OTP: RabbitMQ requer Erlang/OTP para funcionar. Você pode baixar o instalador do Erlang aqui.

    Download e Instalação:
        Acesse a página oficial de download do RabbitMQ: RabbitMQ Downloads.
        Siga as instruções de instalação específicas para o seu sistema operacional (Windows, macOS, Linux).

Inicialização

Para inicializar o RabbitMQ, você pode usar os comandos do sistema ou os aplicativos disponíveis após a instalação local. Caso esteja utilizando um container, a inicialização dependerá do servidor ativo.

Untitled
Conceitos Básicos

    Mensagem: Unidade de dados que é enviada de um produtor para um consumidor.
    Produtor: A aplicação que envia mensagens.
    Consumidor: A aplicação que recebe e processa mensagens.
    Fila (Queue): Armazena mensagens até que sejam consumidas.
    Exchange: Recebe mensagens de produtores e as encaminha para as filas com base em regras definidas (bindings).
    Binding: Relaciona uma exchange a uma fila.

Utilizando RabbitMQ

Passo 1: Iniciar o RabbitMQ

Após a instalação, inicie o servidor RabbitMQ.

No Windows, através do prompt de comando:

shell

rabbitmq-server start

No Linux ou macOS, use:

shell

sudo systemctl start rabbitmq-server

Passo 2: Acessar a RabbitMQ Management Interface

Por padrão, a interface de gerenciamento do RabbitMQ está disponível em http://localhost:15672. O usuário padrão é guest e a senha é guest.
Exemplo de Uso com Python (Pika Library)

Instalação da Biblioteca Pika:

shell

pip install pika

Código do Produtor:

python

import pika

# Conectar ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar uma fila chamada 'hello'
channel.queue_declare(queue='hello')

# Enviar uma mensagem 'Hello World!'
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()

Código do Consumidor:

python

import pika

# Conectar ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar uma fila chamada 'hello'
channel.queue_declare(queue='hello')

# Definir a função de callback que será chamada ao receber uma mensagem
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Consumir mensagens da fila 'hello'
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

Exemplos de Uso Comum

    Processamento Assíncrono:
        Utilizado para dividir tarefas longas em partes menores e processá-las de forma assíncrona.
    Comunicação entre Microservices:
        RabbitMQ facilita a comunicação entre diferentes microservices, melhorando a escalabilidade e resiliência do sistema.
    Fila de Tarefas:
        Implementação de filas de tarefas onde produtores enviam tarefas para filas e consumidores processam essas tarefas.

Exemplo de Uso no Vision4Docs/Processos Transacionais

Contexto:

No Vision4Docs, nosso produto analisa transações para detectar se são fraudulentas ou não. Utilizamos RabbitMQ para otimizar esse processo de análise.

Processo:

    Envio de Transações:
        Transações são enviadas para uma fila no RabbitMQ pelo sistema de processamento inicial.

    Análise de Fraude:
        Vários consumidores, que são serviços de análise de fraude, lêem as mensagens (transações) da fila.
        Cada serviço analisa a transação e determina se é fraudulenta ou não.

    Benefícios:
        Otimização: As transações são processadas de forma assíncrona, permitindo que o sistema de processamento inicial continue operando sem esperar pela análise de fraude.
        Escalabilidade: Facilita a adição de mais consumidores (serviços de análise) conforme necessário para lidar com volumes maiores de transações.
        Direcionamento Correto: As mensagens podem ser roteadas para filas diferentes com base em critérios específicos, garantindo que cada transação seja analisada pelo serviço apropriado.

