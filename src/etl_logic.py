import pandas as pd
import os

#Metodo que lee el tipo de encoding para evitar errores de lectura
def smart_read_csv(file_path) -> pd.DataFrame:
    with open(file_path,'rb') as f:
        res = chardet.detect(f.read(1000))

    return pd.read_csv(file_path, encoding=res['encoding'], encoding_errors='replace')

def get_raw_files() -> pd.DataFrame:
    try:
        df_orders = smart_read_csv('../data/orders.csv')
        df_orders_details = smart_read_csv('../data/order_details.csv')
        df_pizzas = smart_read_csv('../data/pizzas.csv')
        df_pizza_types = smart_read_csv('../data/pizza_types.csv')

        print('Files load completed succcesfully')
    except Exception as e:
        print(f"Error: {e}")