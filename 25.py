import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Pot@toGuN1.', db='menagerie')
print("Connected")
cursor = conn.cursor()
select_query = """
SELECT name, birth, MONTH(birth)
FROM pet
"""
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    name, birth, birth_month = row
    print(f"{name},\t{birth},\t\t{birth_month}")
cursor.close()
conn.close()