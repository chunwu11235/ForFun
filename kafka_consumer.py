from kafka import KafkaConsumer
consumer = KafkaConsumer('sample')
while(True):
    for message in consumer:
        print (message)