import psycopg2
from psycopg2 import Error


try:
    connection = psycopg2.connect(user="odoo",
                                  password="code200!",
                                  host="192.168.56.21",
                                  port="5432",
                                  database="MTBL")
    cursor = connection.cursor()
    print("Postgresql Server Information")
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT name,debit,credit FROM account_move_line;")
    record = cursor.fetchall()
    for val in record:
        print("Journal Name:{0}, Debit: {1}, Credit: {2}".format(val[0],val[1],val[2]))

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Postgresql connection is closed")
