import mysql.connector as mc

conn = mc.connect(
    host='localhost',
    user='root',
    password='Pot@toGuN1.'
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

for database in cursor:
    print(database[0])

cursor.close()
conn.close()