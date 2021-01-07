import random, string, time
from json import dumps
from kafka import KafkaProducer

COUNT = 10000000
KF_IP = ['192.168.56.22:9092']
producer = KafkaProducer(bootstrap_servers=KF_IP, value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(COUNT):
    username = str(e) + ''.join(random.choice(string.ascii_letters) for i in range(5))
    password = ''.join(random.choice(string.ascii_letters) for i in range(50))
    data = {'username': username, 'password': password, 'full_name': username}
    print("-----------------------{0}".format(e))
    producer.send('numtest', value=data)
