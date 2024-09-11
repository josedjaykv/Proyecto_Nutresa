import pandas as pd

# Cargar el archivo original, forzando todas las columnas a ser leídas como texto
df = pd.read_csv('Data/materia_prima.csv', delimiter=';')

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Date'] = df['Date'].astype(str)
df['Precio_cacao_und'] = df['Precio_cacao_und'].str.replace(',', '.').astype(float)
df['Precio_cacao_und'].fillna(0, inplace=True)
df['Precio_cacao_und'] = df['Precio_cacao_und'].astype(int)

df['Precio_cafe'] = df['Precio_cafe'].str.replace(',', '.').astype(float)
df['Precio_cafe'].fillna(0, inplace=True)
df['Precio_cafe'] = df['Precio_cafe'].astype(int)

df['Precio_carne_cerdo'] = df['Precio_carne_cerdo'].str.replace(',', '.').astype(float)
df['Precio_carne_cerdo'].fillna(0, inplace=True)
df['Precio_carne_cerdo'] = df['Precio_carne_cerdo'].astype(int)

df['Precio_carne_res'] = df['Precio_carne_res'].str.replace(',', '.').astype(float)
df['Precio_carne_res'].fillna(0, inplace=True)
df['Precio_carne_res'] = df['Precio_carne_res'].astype(int)
    

df_filtered = df[['Date', 'Precio_cacao_und', 'Precio_cafe', 'Precio_carne_cerdo', 'Precio_carne_res']]

df_filtered.to_csv('NewData/newMateria_prima.csv', index=False)

print("Archivo 'newdf.csv' creado con éxito.")
