import pandas as pd

df = pd.read_csv('Data/Diesel_flota_logistica.csv', sep=';')

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Precio'] = df['Precio'].str.replace(',', '.').astype(float)

df['Year-Month'] = df['Date'].dt.to_period('M')

promedio_mensual = df.groupby('Year-Month')['Precio'].mean().reset_index()

promedio_mensual.to_csv('NewData/Disel_precio.csv', index=False)

print("Nuevo archivo CSV con columnas 'Date' y 'Precio' creado exitosamente.")
