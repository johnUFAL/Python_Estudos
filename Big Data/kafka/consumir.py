from kafka import KafkaConsumer

# Conf, endereço e porta do servidor kafka
bootstrap_servers = 'localhost:9092'

# Tópico de envio das mensagens 
topico = 'meu-topico'

# Crinado o consumidor
consumer = KafkaConsumer(topico, bootstrap_servers=bootstrap_servers)

# Consumir mensagem para o kafka
for mensagem in range(5):
    print(f'Mensgame recebida: {mensagem.value.decode('utf-8')}')

# Fechando o produtor 
consumer.close()