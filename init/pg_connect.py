import psycopg2
from psycopg2 import Error

PG_USER = "odoo"
PG_PASS = "code200!"
PG_HOST = "192.168.56.21"
PG_PORT = "5432"
PG_DB = "MTBL"

try:
    connection = psycopg2.connect(user=PG_USER, password=PG_PASS, host=PG_HOST, port=PG_PORT, database=PG_DB)
    cursor = connection.cursor()

    cursor.execute("SELECT name,debit,credit FROM account_move_line;")
    record = cursor.fetchall()

    for val in record:
        print("Journal Name:{0}, Debit: {1}, Credit: {2}".format(val[0], val[1], val[2]))

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Postgresql connection is closed")
