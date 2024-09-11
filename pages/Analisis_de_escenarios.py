import streamlit as st
import login
import pandas as pd

login.generar_login()
if 'usuario' in st.session_state:
    st.header('Analisis de :orange[escenarios]')
    
    st.write("Escenarios de costos de diferentes módulos bajo diferentes trayectorias climáticas")

    #datos
    Promedio_energia = pd.read_csv('NewData/Promedio_Energia.csv')
    precio_energia = pd.read_csv('Data/precio_energia.csv', sep=';')
    
    st.subheader("Consumo de :orange[Energía Promedio Mensual]")
    st.line_chart(Promedio_energia.set_index('Mes'))
    
    
    precio_energia['Date'] = pd.to_datetime(precio_energia['Date'], dayfirst=True)
    precio_energia = precio_energia.sort_values(by='Date')
    
    st.subheader("Precio de la :orange[Energía]")
    st.line_chart(precio_energia.set_index('Date'))
