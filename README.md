# Trilha de Conhecimento: RabbitMQ

## Objetivo

Este guia visa fornecer uma introdução completa ao RabbitMQ, explicando o que é, como instalá-lo, utilizá-lo e exemplos de usos comuns.

---

## O que é RabbitMQ?

RabbitMQ é um message broker de código aberto que implementa o Advanced Message Queuing Protocol (AMQP). Ele facilita a comunicação entre diferentes partes de um sistema distribuído, permitindo que as mensagens sejam enviadas e recebidas de forma assíncrona.

---

## Instalação do RabbitMQ

### Pré-requisitos

- **Erlang/OTP**: RabbitMQ requer Erlang/OTP para funcionar. Você pode baixar o instalador do Erlang [aqui](https://www.erlang.org/downloads).

### Download e Instalação

1. Acesse a página oficial de download do RabbitMQ: [RabbitMQ Downloads](https://www.rabbitmq.com/download.html).
2. Siga as instruções de instalação específicas para o seu sistema operacional (Windows, macOS, Linux).

### Inicialização

Você realiza a inicialização do servidor local através dos próprios aplicativos que serão exibidos no seu sistema, caso tenha sido feita a instalação local. No caso da aplicação em container, funcionaria de acordo com o servidor ativo. Esses ícones servem para executar comandos em seu prompt nativo e subir a URL necessária para o uso do RabbitMQ.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/65f34d99-828f-4c90-b13e-56fd4374a1c3/7fa6f9b6-1fc2-4bdc-a92d-3da43f30ea1d/Untitled.png)

---

## Conceitos Básicos

- **Mensagem**: Unidade de dados que é enviada de um produtor para um consumidor.
- **Produtor**: A aplicação que envia mensagens.
- **Consumidor**: A aplicação que recebe e processa mensagens.
- **Fila (Queue)**: Armazena mensagens até que sejam consumidas.
- **Exchange**: Recebe mensagens de produtores e as encaminha para as filas com base em regras definidas (bindings).
- **Binding**: Relaciona uma exchange a uma fila.

---

## Utilizando RabbitMQ

### Passo 1: Iniciar o RabbitMQ

Após a instalação, inicie o servidor RabbitMQ. No Windows, isso pode ser feito através do prompt de comando:

No Linux ou macOS, use:

### Passo 2: Acessar o RabbitMQ Management Interface

Por padrão, a interface de gerenciamento do RabbitMQ está disponível em `http://localhost:15672`. O usuário padrão é `guest` e a senha é `guest`.

---

## Exemplo de Uso no Vision4Docs/Processos Transacionais

### Contexto

No Vision4Docs, nosso produto analisa transações para detectar se são fraudulentas ou não. Utilizamos RabbitMQ para otimizar esse processo de análise.

### Processo

1. **Envio de Transações**:
    - Transações são enviadas para uma fila no RabbitMQ pelo sistema de processamento inicial.
2. **Análise de Fraude**:
    - Vários consumidores, que são serviços de análise de fraude, lêem as mensagens (transações) da fila.
    - Cada serviço analisa a transação e determina se é fraudulenta ou não.
3. **Benefícios**:
    - **Otimização**: As transações são processadas de forma assíncrona, permitindo que o sistema de processamento inicial continue operando sem esperar pela análise de fraude.
    - **Escalabilidade**: Facilita a adição de mais consumidores (serviços de análise) conforme necessário para lidar com volumes maiores de transações.
    - **Direcionamento Correto**: As mensagens podem ser roteadas para filas diferentes com base em critérios específicos, garantindo que cada transação seja analisada pelo serviço apropriado.

---

## Exemplos de Uso Comum

1. **Processamento Assíncrono**:
    - Utilizado para dividir tarefas longas em partes menores e processá-las de forma assíncrona.
2. **Comunicação entre Microservices**:
    - RabbitMQ facilita a comunicação entre diferentes microservices, melhorando a escalabilidade e resiliência do sistema.
3. **Fila de Tarefas**:
    - Implementação de filas de tarefas onde produtores enviam tarefas para filas e consumidores processam essas tarefas.


## Utilizando RabbitMQ

**Passo 1: Iniciar o RabbitMQ**

Após a instalação, inicie o servidor RabbitMQ. No Windows, isso pode ser feito através do prompt de comando:
```
rabbitmq-server start
```
