import sqlite3
import csv

# Conectar a la base de datos (si no existe, se crea)
conn = sqlite3.connect('nutresa.db')
cursor = conn.cursor()

# Crear la tablas

# diesel_flota_logistica
cursor.execute('''
CREATE TABLE IF NOT EXISTS Diesel_flota_logistica (
    Date TEXT,
    Producto TEXT,
    Cantidad REAL,
    Cantidad_prom REAL,
    Precio REAL,
    Total_Venta REAL,
    Kilometraje REAL
);
''')
#Energia diaria
cursor.execute('''
CREATE TABLE IF NOT EXISTS energia_diaria (
    Date TEXT,
    Total_Nutresa REAL
);
''')
#Insumos
cursor.execute('''
CREATE TABLE IF NOT EXISTS insumos (
    Date TEXT,
    Ton_prod_nutresa REAL,
    Carbon_nutresa REAL,
    Diesel_ACPM_nutresa REAL,
    GLP_nutresa REAL,
    gas_nutresa REAL,
    gasolina_nutresa REAL,
    C_Carbon_nutresa REAL,
    C_Diesel_nutresa REAL,
    C_GLP_liquido_nutresa REAL,
    C_GLP_gasesoso_nutresa REAL,
    C_gas_nutresa REAL,
    C_gasolina_nutresa REAL,
    energia_termica_nutresa REAL,
    energia_electrica_nutresa REAL,
    Emisiones REAL
);
''')

#materia prima
cursor.execute('''
CREATE TABLE IF NOT EXISTS materia_prima (
    Date TEXT,
    cacao_nal INTEGER,
    Precio_cacao_und REAL,
    cantidad_cacao REAL,
    cafe_nal INTEGER,
    Precio_cafe REAL,
    cantidad_cafe REAL,
    cerdo_nal INTEGER,
    Precio_carne_cerdo REAL,
    cantid_carne_cerdo REAL,
    res_nal INTEGER,
    Precio_carne_res REAL,
    cant_carne_res REAL
);
''')

#precio energía
cursor.execute('''
CREATE TABLE IF NOT EXISTS precio_energia (
    Date TEXT,
    precio_nutresa REAL
);
''')


#insertar datos
def insertar_datos_Diesel_flota_logistica(db_name, csv_file):
   
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Función para convertir una cadena a float, manejando valores vacíos
    def convertir_a_float(valor):
        try:
            return float(valor.replace(',', '.')) if valor else 0.0
        except ValueError:
            return 0.0  # Retorna 0.0 en caso de que no se pueda convertir

    # Abre el archivo CSV
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        
        # Salta la primera fila si contiene los encabezados
        next(reader)
        
        
        for row in reader:
            date = row[0]
            producto = row[1]
            cantidad = convertir_a_float(row[2])
            cantidad_prom = convertir_a_float(row[3])
            precio = convertir_a_float(row[4])
            total_venta = convertir_a_float(row[5])
            kilometraje = convertir_a_float(row[6])
            
            
            cursor.execute('''
                INSERT INTO Diesel_flota_logistica (Date, Producto, Cantidad, Cantidad_prom, Precio, Total_Venta, Kilometraje)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (date, producto, cantidad, cantidad_prom, precio, total_venta, kilometraje))

    
    conn.commit()
    conn.close()
    
    
def insertar_datos_energia_diaria(db_name, csv_file):
   
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        
        
        next(reader)
        
        
        for row in reader:
            Date = row[0]
            total_nutresa = row[1]
            
           
            cursor.execute('''
                INSERT INTO energia_diaria (Date, Total_Nutresa)
                VALUES (?, ?)
            ''', (Date, total_nutresa))

   
    conn.commit()
    conn.close()


def insertar_datos_insumos(db_name, csv_file):
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Función para convertir una cadena a float, manejando valores vacíos
    def convertir_a_float(valor):
        try:
            return float(valor.replace(',', '.')) if valor else 0.0
        except ValueError:
            return 0.0  # Retorna 0.0 en caso de que no se pueda convertir

    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        
        
        next(reader)
        
        
        for row in reader:
            date = row[0]
            ton_prod_nutresa = convertir_a_float(row[1])
            carbon_nutresa = convertir_a_float(row[2])
            diesel_acpm_nutresa = convertir_a_float(row[3])
            glp_nutresa = convertir_a_float(row[4])
            gas_nutresa = convertir_a_float(row[5])
            gasolina_nutresa = convertir_a_float(row[6])
            c_carbon_nutresa = convertir_a_float(row[7])
            c_diesel_nutresa = convertir_a_float(row[8])
            c_glp_liquido_nutresa = convertir_a_float(row[9])
            c_glp_gasesoso_nutresa = convertir_a_float(row[10])
            c_gas_nutresa = convertir_a_float(row[11])
            c_gasolina_nutresa = convertir_a_float(row[12])
            energia_termica_nutresa = convertir_a_float(row[13])
            energia_electrica_nutresa = convertir_a_float(row[14])
            emisiones = convertir_a_float(row[15])
            
            
            cursor.execute('''
                INSERT INTO insumos (Date, Ton_prod_nutresa, Carbon_nutresa, Diesel_ACPM_nutresa, GLP_nutresa, gas_nutresa, gasolina_nutresa,
                C_Carbon_nutresa, C_Diesel_nutresa, C_GLP_liquido_nutresa, C_GLP_gasesoso_nutresa, C_gas_nutresa, C_gasolina_nutresa,
                energia_termica_nutresa, energia_electrica_nutresa, Emisiones)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, ton_prod_nutresa, carbon_nutresa, diesel_acpm_nutresa, glp_nutresa, gas_nutresa, gasolina_nutresa,
                  c_carbon_nutresa, c_diesel_nutresa, c_glp_liquido_nutresa, c_glp_gasesoso_nutresa, c_gas_nutresa,
                  c_gasolina_nutresa, energia_termica_nutresa, energia_electrica_nutresa, emisiones))

   
    conn.commit()
    conn.close()


def insertar_datos_materia_prima(db_name, csv_file):
     
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Función para convertir una cadena a float, manejando valores vacíos
    def convertir_a_float(valor):
        try:
            # Verificar si el valor está vacío y reemplazarlo por 0.0
            return float(valor.replace(',', '.')) if valor and valor.strip() != '' else 0.0
        except ValueError:
            return 0.0  # Retorna 0.0 en caso de que no se pueda convertir

    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        
        # Salta la primera fila si contiene los encabezados
        next(reader)
        
    
        for row in reader:
            
            try:
                date = row[0]
                cacao_nal = convertir_a_float(row[1])
                precio_cacao_und = convertir_a_float(row[2])
                cantidad_cacao = convertir_a_float(row[3])
                cafe_nal = convertir_a_float(row[4])
                precio_cafe = convertir_a_float(row[5])
                cantidad_cafe = convertir_a_float(row[6])
                cerdo_nal = convertir_a_float(row[7])
                precio_carne_cerdo = convertir_a_float(row[8])
                cantidad_carne_cerdo = convertir_a_float(row[9])
                res_nal = convertir_a_float(row[10])
                precio_carne_res = convertir_a_float(row[11])
                cantidad_carne_res = convertir_a_float(row[12])
                
               
                cursor.execute('''
                    INSERT INTO materia_prima (Date, cacao_nal, Precio_cacao_und, cantidad_cacao, cafe_nal, Precio_cafe, cantidad_cafe, 
                    cerdo_nal, Precio_carne_cerdo, cantid_carne_cerdo, res_nal, Precio_carne_res, cant_carne_res)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (date, cacao_nal, precio_cacao_und, cantidad_cacao, cafe_nal, precio_cafe, cantidad_cafe, cerdo_nal, 
                      precio_carne_cerdo, cantidad_carne_cerdo, res_nal, precio_carne_res, cantidad_carne_res))
            except Exception as e:
                print(f"Error al procesar la fila: {row}. Error: {e}")

    conn.commit()
    conn.close()
    
def insertar_datos_precio_energia(db_name, csv_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        
        # Salta la primera fila si contiene los encabezados
        next(reader)
        
        
        for row in reader:
            Date = row[0]
            precio_nutresa = row[1]
            
            
            cursor.execute('''
                INSERT INTO precio_energia (Date, precio_nutresa)
                VALUES (?, ?)
            ''', (Date, precio_nutresa))

    
    conn.commit()
    conn.close()

# Uso de la función

#insertar_datos_energia_diaria('nutresa.db', '../Data/energia_diaria.csv')
#insertar_datos_Diesel_flota_logistica('nutresa.db', '../Data/Diesel_flota_logistica.csv')
#insertar_datos_insumos('nutresa.db', '../Data/insumos.csv')
#insertar_datos_materia_prima('nutresa.db', '../Data/materia_prima.csv')
#insertar_datos_precio_energia('nutresa.db', '../Data/precio_energia.csv')


conn.commit()

# Cerrar la conexión
conn.close()