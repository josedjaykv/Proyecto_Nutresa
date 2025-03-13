import streamlit as st
from streamlit_echarts import st_echarts
import login
import pandas as pd
import sqlite3

if False:
    """
    def obtener_datos(query):
        conn=sqlite3.connect('database/nutresa.db')
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    """
login.generar_login()
if 'usuario' in st.session_state:
    st.header('Analisis de :orange[escenarios]')
    st.write("Escenarios de costos de diferentes módulos bajo diferentes trayectorias climáticas")
    
    
    #datos
    Promedio_energia = pd.read_csv('NewData/Promedio_Energia.csv')
    precio_energia = pd.read_csv('Data/precio_energia.csv', sep=';')
    Materia_prima = pd.read_csv('NewData/newMateria_prima.csv')
    Disel_precio = pd.read_csv('NewData/Disel_precio.csv')
    Energia_termica = pd.read_csv('NewData/Energia_termica.csv')
    Emisiones = pd.read_csv('NewData/Emisiones.csv')
    
    st.subheader("Consumo de :orange[Energía Promedio Mensual]")
    st.line_chart(Promedio_energia.set_index('Mes'))
    
    precio_energia['Date'] = pd.to_datetime(precio_energia['Date'], dayfirst=True)
    precio_energia = precio_energia.sort_values(by='Date')
    st.subheader("Precio de la :orange[Energía]")
    st.line_chart(precio_energia.set_index('Date'))

    st.subheader("Combustible flota :orange['Disel']")
    st.line_chart(Disel_precio.set_index('Year-Month'))
    
    st.subheader("Energía térmica :orange[Nutresa]")
    st.line_chart(Energia_termica.set_index('Date'))

    
    st.subheader("Emisiones de :orange[CO2]")
    st.line_chart(Emisiones.set_index('Date'))
    
    
    st.subheader("Costo de :orange[Materia Prima]")

    options = {
        "title": {"text": ""},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
        },
        "legend": {"data": ['Precio_cacao_und', 'Precio_cafe', 'Precio_carne_cerdo', 'Precio_carne_res']},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "grid": {"left": "3%", "right": "3%", "bottom": "3%", "containLabel": True},
        "xAxis": [
            {
                "type": "category",
                "boundaryGap": False,
                "data":  Materia_prima['Date'].tolist(),
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "name": 'Precio_cacao_und',
                "type": "line",
                "stack": "total",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": Materia_prima['Precio_cacao_und'].tolist(),
            },
            {
                "name": 'Precio_cafe',
                "type": "line",
                "stack": "total",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": Materia_prima['Precio_cafe'].tolist(),
            },
            {
                "name": 'Precio_carne_cerdo',
                "type": "line",
                "stack": "total",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": Materia_prima['Precio_carne_cerdo'].tolist(),
            },
            {
                "name": 'Precio_carne_res',
                "type": "line",
                "stack": "total",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": Materia_prima['Precio_carne_res'].tolist(),
            },
        ],
    }

# Mostrar el gráfico en Streamlit
st_echarts(options=options, height="400px", width="100%")

if False:
    """
    #New extraction of data
    Promedio_energia = obtener_datos('''SELECT
        strftime('%Y-%m', 
                 substr(Date, 7, 4) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2)) AS mes,  
        AVG(Total_Nutresa) AS promedio_energia  
    FROM energia_diaria
    WHERE Total_Nutresa IS NOT NULL  
    GROUP BY mes
    ORDER BY mes;''')
    
    precio_energia = obtener_datos('''SELECT * FROM precio_energia;''')
    
    
    Diesel_precio = obtener_datos('''
    SELECT 
        strftime('%Y-%m', 
                 substr(Date, 7, 4) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2)) AS "YearMonth", 
        AVG(Precio) AS Precio
    FROM Diesel_flota_logistica
    GROUP BY "YearMonth"
    ORDER BY "YearMonth";
''')
    Energia_termica = obtener_datos('''
    SELECT 
        strftime('%Y-%m-%d', 
                 substr(Date, 7, 4) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2)) AS Date, 
        energia_termica_nutresa AS Energia_termica
    FROM insumos
    ORDER BY Date ASC;
''')

    
    Emisiones = obtener_datos('''SELECT 
                              strftime('%Y-%m-%d', 
                 substr(Date, 7, 4) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2)) AS Date,
                              Emisiones 
                              FROM insumos
                              ORDER BY Date ASC;''')

    
    #New Graphs
    st.subheader("Consumo de :orange[Energía Promedio Mensual]")
    Promedio_energia.set_index('mes', inplace=True)
    st.line_chart(Promedio_energia['promedio_energia'])
    
    precio_energia['Date'] = pd.to_datetime(precio_energia['Date'], dayfirst=True)
    precio_energia = precio_energia.sort_values(by='Date')
    st.subheader("Precio de la :orange[Energía]")
    st.line_chart(precio_energia.set_index('Date'))
    
    st.subheader("Combustible flota :orange['Diesel']")
    Diesel_precio['YearMonth'] = pd.to_datetime(Diesel_precio['YearMonth'], format='%Y-%m')
    Diesel_precio.set_index('YearMonth', inplace=True)
    st.line_chart(Diesel_precio)
    
    st.subheader("Energía térmica :orange[Nutresa]")
    st.line_chart(Energia_termica.set_index('Date'))
    
    st.subheader("Emisiones de :orange[CO2]")
    st.line_chart(Emisiones.set_index('Date'))
    
    
    


    """   


    

    

    
   