# Gestión de base de datos SQLite

import sqlite3

def initialize_database():
    # Crear la base de datos y la tabla
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()

    # Crear la tabla para guardar archivos y etiquetas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS archivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direccion TEXT NOT NULL,
            etiqueta TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
