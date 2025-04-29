import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sveikatos_istorijos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ligos_istorija TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vardas TEXT NOT NULL,
    pavarde Text NOT NULL,
    amzius INTEGER NOT NULL,
    sveikatos_istorijos_id INTEGER NOT NULL,
    FOREIGN KEY (sveikatos_istorijos_id) REFERENCES sveikatos_istorijos(id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS darbuotojai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vardas TEXT NOT NULL,
    pavarde Text NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pavadinimas TEXT NOT NULL
);
''')


cursor.execute('''
ALTER TABLE darbuotojai ADD COLUMN amzius integer
''')


cursor.execute('''
ALTER TABLE darbuotojai ADD COLUMN roles_id integer
''')

# cursor.execute('''
# ALTER TABLE darbuotojai ADD CONSTRAINT fk_roles FOREIGN KEY (roles_id) REFERENCES roles(id)
# ''')

cursor.execute('''
INSERT INTO roles (pavadinimas) VALUES ("admin")
''')

cursor.execute('''
INSERT INTO roles (pavadinimas) VALUES ("simple_user")
''')

cursor.execute('''
DELETE FROM roles WHERE id = 1
''')

cursor.execute('''
UPDATE roles SET pavadinimas = "papratas_vartotojas" WHERE id = 2
''')

conn.commit()

conn.close()

print("Lentelės sukurtos ir duomenys įterpti!")
