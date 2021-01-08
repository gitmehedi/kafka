import random, string, time
from json import dumps
from kafka import KafkaProducer
import psycopg2
from psycopg2 import Error

PG_USER = "odoo"
PG_PASS = "code200!"
PG_HOST = "192.168.56.21"
PG_PORT = "5432"
PG_DB = "MTBL"
COUNT = 200
KF_IP = ['192.168.56.22:9092']

producer = KafkaProducer(bootstrap_servers=KF_IP, value_serializer=lambda x: dumps(x).encode('utf-8'))

connection = psycopg2.connect(user=PG_USER, password=PG_PASS, host=PG_HOST, port=PG_PORT, database=PG_DB)
cursor = connection.cursor()

cursor.execute("SELECT name,debit,credit FROM account_move_line;")
record = cursor.fetchall()

for val in record:
    print("Journal Name:{0}, Debit: {1}, Credit: {2}".format(val[0], val[1], val[2]))
    journal = {'key': 'move', 'ref': val[0], 'credit': val[1], 'debit': val[2]}
    producer.send('cassandra', value=journal)

for e in range(COUNT):
    username = str(e) + ''.join(random.choice(string.ascii_letters) for i in range(5))
    password = ''.join(random.choice(string.ascii_letters) for i in range(50))
    data = {'key': 'test', 'username': username, 'password': password, 'full_name': username}
    print("-----------------------{0}".format(e))
    producer.send('cassandra', value=data)
