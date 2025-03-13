import sqlite3
import bcrypt
import csv

def initialize_database():
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()

    # Crear la tabla de usuarios si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def insert_users_from_csv(csv_file):
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Omitir la primera fila (encabezados)

        for row in reader:
            usuario, nombre, password = row
            hashed_password = hash_password(password)

            try:
                cursor.execute("INSERT INTO usuarios (usuario, nombre, password) VALUES (?, ?, ?)", 
                               (usuario, nombre, hashed_password))
            except sqlite3.IntegrityError:
                print(f"El usuario '{usuario}' ya existe en la base de datos.")

    conn.commit()
    conn.close()

# Ejecutar la inicialización y cargar datos desde el CSV
initialize_database()
insert_users_from_csv("usuarios.csv")

print("Usuarios insertados correctamente.")
