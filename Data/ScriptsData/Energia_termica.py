import pandas as pd

df = pd.read_csv('Data/insumos.csv', sep=';')

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df_filtered = df[['Date', 'energia_termica_nutresa']]

df_filtered.to_csv('NewData/Energia_termica.csv', index=False)

print("Archivo 'Energia_termica.csv' creado con éxito.")