import streamlit as st
import sqlite3
import bcrypt
import pandas as pd
from Home import generarMenu

def mostrar_admin_usuarios():
    if 'usuario' in st.session_state and st.session_state['usuario'] == 'admin':
        st.title('Administración de Usuarios')
        
        # Mostrar usuarios existentes
        conn = sqlite3.connect("database/archivos.db")
        df_usuarios = pd.read_sql_query("SELECT usuario, nombre FROM usuarios", conn)
        st.subheader("Usuarios actuales")
        st.dataframe(df_usuarios)
        
        # Formulario para agregar nuevo usuario
        st.subheader("Agregar nuevo usuario")
        with st.form("nuevo_usuario"):
            nuevo_usuario = st.text_input("Usuario")
            nuevo_nombre = st.text_input("Nombre")
            nueva_password = st.text_input("Contraseña", type="password")
            confirmar_password = st.text_input("Confirmar contraseña", type="password")
            
            submitted = st.form_submit_button("Agregar usuario")
            
            if submitted:
                if not nuevo_usuario or not nuevo_nombre or not nueva_password:
                    st.error("Todos los campos son obligatorios")
                elif nueva_password != confirmar_password:
                    st.error("Las contraseñas no coinciden")
                else:
                    # Verificar si el usuario ya existe
                    cursor = conn.cursor()
                    cursor.execute("SELECT usuario FROM usuarios WHERE usuario = ?", (nuevo_usuario,))
                    if cursor.fetchone():
                        st.error(f"El usuario '{nuevo_usuario}' ya existe")
                    else:
                        # Agregar el nuevo usuario
                        hashed_password = bcrypt.hashpw(nueva_password.encode(), bcrypt.gensalt()).decode()
                        cursor.execute("INSERT INTO usuarios (usuario, nombre, password) VALUES (?, ?, ?)", 
                                      (nuevo_usuario, nuevo_nombre, hashed_password))
                        conn.commit()
                        st.success(f"Usuario '{nuevo_usuario}' agregado exitosamente")
                        st.rerun()
        
        conn.close()
    else:
        st.error("No tienes permiso para acceder a esta página")

if __name__ == "__main__":
    if 'usuario' in st.session_state:
        # Generar el menú lateral
        generarMenu(st.session_state['usuario'])
        # Mostrar el contenido de la página
        mostrar_admin_usuarios()
    else:
        st.warning("Debes iniciar sesión primero")
        st.switch_page("inicio.py")