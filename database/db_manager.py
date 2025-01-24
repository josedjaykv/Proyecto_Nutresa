# Gestión de base de datos SQLite

import sqlite3

DB_PATH = "database/promedios.db"

def initialize_database():
    conn = sqlite3.connect(DB_PATH) # Crear la conexión a la base de datos
    cursor = conn.cursor() # Crear un cursor para ejecutar comandos SQL

    # Crear tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        eia_digital_user TEXT,
        eia_digital_password TEXT                             
    )
    ''')

    # Crear tabla de semestres
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS semestre (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        num_creditos INTEGER,
        promedio REAL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    ''')

    # Crear tabla de materias
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS materia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        semestre_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        creditos INTEGER NOT NULL,
        promedio REAL,
        FOREIGN KEY (semestre_id) REFERENCES semestres (id)
    )
    ''')

    # Crear tabla de notas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calificacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        materia_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        nota REAL NOT NULL,
        FOREIGN KEY (materia_id) REFERENCES materias (id)
    )
    ''')

    conn.commit() # Guardar los cambios
    conn.close() # Cerrar la conexión
