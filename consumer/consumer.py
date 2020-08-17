from kafka import KafkaConsumer
#from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['192.168.56.22:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    print(message)
    #message = message.value
    #collection.insert_one(message)
    #print('{} added to {}'.format(message, collection))
