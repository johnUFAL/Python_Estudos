from kafka import kafkaProducer

# Conf, endereço e porta do servidor kafka
bootstrap_servers = 'localhost:9092'

# Criando produto kafka
producer = kafkaProducer(bootstrap_servers=bootstrap_servers)

# Tópico de envio das mensagens 
topico = 'meu-topico'

# Enviando mensagem para o kafka
for i in range(5):
    mensagem = f'Mensagem de teste {i}'
    producer.send(topico, mensagem.encode('utf-8'))
    print(f'Mensgame enviado: {mensagem}')

# Fechando o produtor 
producer.close()