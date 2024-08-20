import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

file_path = Path(__file__).parent / "login/keys.pkl"
st.write(f"Intentando abrir el archivo: {file_path.absolute()}")

try:
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)
    st.success("Contraseñas cargadas exitosamente")
    st.write(f"Contenido de hashed_passwords: {hashed_passwords}")
except Exception as e:
    st.error(f"Error al cargar las contraseñas: {str(e)}")
    st.error(f"Tipo de error: {type(e)}")
    st.error("Por favor, ejecuta generate_keys.py primero.")
    st.stop()

names = ['Alice', 'Bob', 'Charlie']
usernames = ['alice', 'bob', 'charlie']

credentials = {
    "usernames": {
        username: {"name": name, "password": hashed_password}
        for username, name, hashed_password in zip(usernames, names, hashed_passwords)
    }
}

authenticator = stauth.Authenticate(credentials,
    "some_cookie_name", "some_key", cookie_expiry_days=30)
try:
    name, authentication_status, username = authenticator.login('Login', 'main')
except ValueError as e:
    st.error(f"Error en la autenticación: {str(e)}")
    st.error("Intentando sin especificar ubicación.")
    try:
        name, authentication_status, username = authenticator.login("Login")
    except ValueError as e:
        st.error(f"Segundo intento fallido: {str(e)}")
        st.error("Intentando con 'sidebar' como ubicación.")
        try:
            name, authentication_status, username = authenticator.login("Login", "sidebar")
        except ValueError as e:
            st.error(f"Tercer intento fallido: {str(e)}")
            st.error("La autenticación no pudo ser realizada.")
            name, authentication_status, username = None, False, None

if authentication_status:
    st.write(f'Bienvenido *{name}*')
    st.title('Contenido de la aplicación')
    authenticator.logout('Logout', 'main')
elif authentication_status == False:
    st.error('Usuario/contraseña incorrectos')
elif authentication_status == None:
    st.warning('Por favor, ingresa tu usuario y contraseña')

st.write('Contenido público')