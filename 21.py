import mysql.connector as mc

conn = mc.connect(
    host='localhost',
    user='root',
    password='Pot@toGuN1.',
    database='menagerie'
)

cursor = conn.cursor()
cursor.execute("SELECT name, birth FROM pet")

for record in cursor:
    print(record)

cursor.close()
conn.close()