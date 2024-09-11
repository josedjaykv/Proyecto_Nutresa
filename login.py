import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd

def validarUsuario(user, password):
    dfusuarios= pd.read_csv('usuarios.csv')
    if len(dfusuarios[(dfusuarios['usuario']==user) & (dfusuarios['password']==password)])>0:
        return True
    else:
        return False
    
def generarMenu(usuario):
    with st.sidebar:
        st.image("logoEIA.png", width=100)
        # botón de color rojo
        dfusuarios= pd.read_csv('usuarios.csv')
        dfUsuario = dfusuarios[dfusuarios['usuario']==usuario]
        nombre = dfUsuario['nombre'].values[0]
        st.subheader(f'Bienvenido {nombre}')        

        st.page_link('inicio.py',label='Inicio', icon=':material/home:')
        st.subheader('Tableros')
        st.page_link('pages/Analisis_de_costos.py',label='Analisis de costos', icon=':material/attach_money:')
        st.page_link('pages/Analisis_de_escenarios.py',label='Analisis de escenarios', icon=':material/emergency:')
        st.page_link('pages/Banco_de_datos.py',label='Banco de datos', icon=':material/account_balance:')
        st.page_link('pages/Pronosticos.py',label='Pronosticos', icon=':material/online_prediction:')
        st.page_link('pages/showfiles.py',label='Files', icon=':material/online_prediction:')

        btnSalir = st.button('Salir', type = "primary")
        st.divider()
        if btnSalir:
            st.session_state.clear()    
            st.rerun()


def generar_login():
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario'])
    else:
        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuario')
            parPassword = st.text_input('Password', type='password')
            btnLogin = st.form_submit_button('Login',type='primary')
            if btnLogin:
                if validarUsuario(parUsuario, parPassword):
                    st.session_state['usuario'] = parUsuario
                    st.rerun()
                else:
                    st.error('Usuario o password incorrectos')


# Prueba de menú con libreríoa externa
# https://github.com/okld/streamlit-elements.git
#from streamlit_option_menu import option_menu

# Como sidebar
#selected = option_menu(
#    menu_title=None, # required
#    options=["Inicio", "Analisis de costos", "Analisis de escenarios", "Banco de datos", "Pronosticos"], # required
#    orientation="horizontal",
#)
