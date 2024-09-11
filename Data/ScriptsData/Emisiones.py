import pandas as pd

df = pd.read_csv('Data/insumos.csv', sep=';')

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df_filtered = df[['Date', 'Emisiones']]

df_filtered.to_csv('NewData/Emisiones.csv', index=False)

print("Archivo 'Emisiones.csv' creado con éxito.")