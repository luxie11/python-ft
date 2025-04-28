import sqlite3

conn = sqlite3.connect('cars2.db')
cursor = conn.cursor()

# cursor.execute('SELECT * FROM cars')
# cursor.execute('SELECT * FROM cars c WHERE c.make = "Audi"')
# cursor.execute('SELECT * FROM cars c WHERE c.year > 2002')
# cursor.execute('SELECT * FROM cars c WHERE make LIKE "F%"')
# cursor.execute('SELECT * FROM cars c WHERE color IS NOT NULL')
print("PIRMA UZKLAUSA:")
cursor.execute('SELECT * FROM cars c ORDER BY year ASC')
rows1 = cursor.fetchall()
print("Antra UZKLAUSA:")
cursor.execute('SELECT MIN(price) FROM cars c ')
rows2 = cursor.fetchall()

# suma = 0;
# for row in rows:
#     suma=suma+row[4]

for row in rows2:
    print(row)

conn.close()
