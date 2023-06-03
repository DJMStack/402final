import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Pot@toGuN1.', db='menagerie')
print("Connected")
cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS menagerie')
print("dropped database")
table = cursor.fetchall()
conn.commit()
print("close app")
cursor.close()
conn.close()