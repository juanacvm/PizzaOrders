from config import db_driver, server, db_name, user, password
from sqlalchemy import create_engine 
import urllib

#Parametros necesarios para la conexión a SQL
param = (
        f"DRIVER={{{db_driver}}};"
        f"SERVER={server};"
        f"DATABASE={db_name};"
        f"UID={user};"
        f"PWD={password};"
        "TrustServerCertificate=yes;"
    )

connection_string = urllib.parse.quote_plus(param)

#Crea la cadena de conexión
url = f"mssql+pyodbc:///?odbc_connect={connection_string}"

#Ejecuta la conexión a la base de datos
engine = create_engine(url,fast_executemany=True)