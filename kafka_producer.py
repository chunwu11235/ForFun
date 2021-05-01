# todo: migrate to confluent-kafka
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
try:
    for i in range(100):
        message = "Hello World {} time".format(i)
        producer.send('sample', str.encode(message))
except Exception as e:
    print(e)

producer.flush(20)