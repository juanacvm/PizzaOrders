from config import db_driver, server, db_name, user, password
from sqlalchemy import create_engine, text
import urllib

#Parametros necesarios para la conexión a SQL
param = (
        f"DRIVER={{{db_driver}}};"
        f"SERVER={server};"
        f"UID={user};"
        f"PWD={password};"
        "TrustServerCertificate=yes;"
    )

connection_string = urllib.parse.quote_plus(param)

#Crea la cadena de conexión
url = f"mssql+pyodbc:///?odbc_connect={connection_string}"

#Ejecuta la conexión a la base de datos
engine = create_engine(url,fast_executemany=True,isolation_level="AUTOCOMMIT")

sql_query = f"""
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{db_name}')
BEGIN
    CREATE DATABASE [{db_name}];
END
"""

def create_database(engine, sql_query):
    try:
        with engine.connect() as conn:
            conn.execute(text(sql_query))
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

param_master = param + f"DATABASE={db_name};" 
connection_string_master = urllib.parse.quote_plus(param_master)
url_master = f"mssql+pyodbc:///?odbc_connect={connection_string_master}"

# Este es el engine que usarás para tus tablas
engine_master = create_engine(url_master, fast_executemany=True)