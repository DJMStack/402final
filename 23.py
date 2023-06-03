import mysql.connector as mc

conn = mc.connect(
    host='localhost',
    user='root',
    password='Pot@toGuN1.',
    database='menagerie'
)

cursor = conn.cursor()
cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")

for record in cursor:
    print(record)

cursor.close()
conn.close()