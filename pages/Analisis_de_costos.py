import streamlit as st
import login
import pandas as pd

login.generar_login()
if 'usuario' in st.session_state:
    st.header('Análisis de :orange[costos]')

    st.write("Análisis de costos de los distintos productos que se manejan")


    precios_info = pd.read_csv('Data/materia_prima.csv', sep=';')

  
    precios_info['Date'] = pd.to_datetime(precios_info['Date'], format='%d/%m/%Y', errors='coerce')

 
    precios_info['Precio_cacao_un'] = precios_info['Precio_cacao_und'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_cac'] = precios_info['cantidad_cacao'].astype(str).str.replace(',', '').astype(float)
    precios_info['Precio_caf'] = precios_info['Precio_cafe'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_caf'] = precios_info['cantidad_cafe'].astype(str).str.replace(',', '').astype(float)
    precios_info['Precio_carne_cerd'] = precios_info['Precio_carne_cerdo'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_carne_cer'] = precios_info['cantid_carne_cerdo'].astype(str).str.replace(',', '').astype(float)
    precios_info['Precio_carne_re'] = precios_info['Precio_carne_res'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_carne_r'] = precios_info['cant_carne_res'].astype(str).str.replace(',', '').astype(float)



    precios_info['VentasCacao'] = precios_info['Precio_cacao_un'] * precios_info['cantidad_cac']
    precios_info['VentasCafe'] = precios_info['Precio_caf'] * precios_info['cantidad_caf']
    precios_info['VentasCarneCerdo'] = precios_info['Precio_carne_cerd'] * precios_info['cantidad_carne_cer']
    precios_info['VentasCarneRes'] = precios_info['Precio_carne_re'] * precios_info['cantidad_carne_r']

  
    st.write(precios_info.head())
    st.write(precios_info.info())
   

    precios_info = precios_info.set_index('Date')

    st.header('Análisis de :orange[costos a lo largo del tiempo]')

    st.subheader("Precios del :orange[Cacao] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_cacao_und'], height=400, width=700)

    st.subheader("Precios del :orange[Café] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_cafe'], height=400, width=700)

    st.subheader("Precios de la :orange[Carne de cerdo] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_carne_cerdo'], height=400, width=700)

    st.subheader("Precios de la :orange[Carne de res] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_carne_res'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Cacao] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCacao'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Café] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCafe'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Carne de cerdo] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCarneCerdo'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Carne de res] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCarneRes'], height=400, width=700)



