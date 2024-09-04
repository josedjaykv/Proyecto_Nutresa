import pandas as pd

energia_diaria = pd.read_csv('Data/energia_diaria.csv', sep=';')

energia_diaria['Date'] = pd.to_datetime(energia_diaria['Date'], dayfirst=True)

energia_diaria['Year-Month'] = energia_diaria['Date'].dt.to_period('M')

promedio_mensual = energia_diaria.groupby('Year-Month')['Total_Nutresa'].mean().reset_index()

matriz_promedio_mensual = promedio_mensual.values.tolist()

pd.DataFrame(matriz_promedio_mensual, columns=['Mes', 'Promedio de Consumo']).to_csv('NewData/Promedio_Energia.csv', index=False)

print(matriz_promedio_mensual)
