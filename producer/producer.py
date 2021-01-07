from time import sleep
from json import dumps
from kafka import KafkaProducer
import random,string,time

COUNT = 10
producer = KafkaProducer(bootstrap_servers=['192.168.56.22:9092'],value_serializer=lambda x:dumps(x).encode('utf-8'))

for e in range(COUNT):
    username = str(e)+''.join(random.choice(string.ascii_letters) for i in range(5))
    password = ''.join(random.choice(string.ascii_letters) for i in range(50))
    data = {'username': username,'password': password, 'full_name': full_name }
    producer.send('data',value=data)
