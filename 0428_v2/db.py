import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS brands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_id INTEGER,
    name TEXT NOT NULL,
    year INTEGER,
    FOREIGN KEY (brand_id) REFERENCES brands(id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER,
    color TEXT,
    price REAL,
    FOREIGN KEY (model_id) REFERENCES models(id)
);
''')

cursor.executemany('''
INSERT INTO brands (name) VALUES (?)
''', [
    ("Audi",),
    ("BMW",),
    ("Toyota",),
    ("Ford",),
    ("Mercedes",)
])

cursor.executemany('''
INSERT INTO models (brand_id, name, year) VALUES (?, ?, ?)
''', [
    (1, "A3", 2020),
    (1, "A4", 2021),
    (2, "X5", 2021),
    (2, "X3", 2020),
    (3, "Corolla", 2022),
    (3, "Camry", 2021),
    (4, "Mustang", 2020),
    (4, "F-150", 2022),
    (5, "C-Class", 2021),
    (5, "E-Class", 2022)
])

cursor.executemany('''
INSERT INTO cars (model_id, color, price) VALUES (?, ?, ?)
''', [
    (1, "Red", 25000),
    (1, "Blue", 27000),
    (2, "Black", 32000),
    (2, "White", 33000),
    (3, "Silver", 55000),
    (3, "Grey", 56000),
    (4, "Yellow", 40000),
    (4, "Red", 42000),
    (5, "Blue", 35000),
    (5, "White", 37000)
])

conn.commit()

conn.close()

print("Lentelės sukurtos ir duomenys įterpti!")
