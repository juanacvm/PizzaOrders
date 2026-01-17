import pandas as pd
import chardet
import os

#Metodo que lee el tipo de encoding para evitar errores de lectura
def smart_read_csv(file_path) -> pd.DataFrame:
    with open(file_path,'rb') as f:
        res = chardet.detect(f.read(1000))

    return pd.read_csv(file_path, encoding=res['encoding'], encoding_errors='replace')

def get_orders_raw_data() -> pd.DataFrame:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__)) #busca la direccion actual del script main
        file_path = os.path.join(script_dir,'../data/orders.csv') #busca la direccion del archivo .csv
        raw_orders = smart_read_csv(file_path)

        return raw_orders
    except FileNotFoundError as e:
        print(f"Error: {e}")

def get_orders_detail_raw_data() -> pd.DataFrame:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__)) #busca la direccion actual del script main
        file_path = os.path.join(script_dir,'../data/order_details.csv') #busca la direccion del archivo .csv
        raw_order_details = smart_read_csv(file_path)

        return raw_order_details
    except FileNotFoundError as e:
        print(f"Error: {e}")

def get_pizzas_raw_data() -> pd.DataFrame:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__)) #busca la direccion actual del script main
        file_path = os.path.join(script_dir,'../data/pizzas.csv') #busca la direccion del archivo .csv
        raw_pizza = smart_read_csv(file_path)

        return raw_pizza
    except FileNotFoundError as e:
        print(f"Error: {e}")

def get_pizzas_types_raw_data() -> pd.DataFrame:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__)) #busca la direccion actual del script main
        file_path = os.path.join(script_dir,'../data/pizza_types.csv') #busca la direccion del archivo .csv
        raw_pizza_types = smart_read_csv(file_path)

        return raw_pizza_types
    except FileNotFoundError as e:
        print(f"Error: {e}")


def build_analytical_orders_data(raw_orders, raw_order_details, raw_pizza, raw_pizza_types) -> pd.DataFrame:
    #Une la cabecera los pedidos con el detalle del pedido
    raw_orders_master = pd.merge(raw_orders, raw_order_details, how="left", on="order_id")

    #Une él codigo de pizza con el tipo de pizza que representa (sus características)
    raw_pizza_master = pd.merge(raw_pizza, raw_pizza_types, how= "left", on="pizza_type_id")

    #Genera la sábana completa de pedidos, en la cual se añade información de las pizzas solicitadas
    df_master = pd.merge(raw_orders_master, raw_pizza_master, how="left", on="pizza_id")

    return df_master

def transform_and_format_orders_data(df_master) -> pd.DataFrame:
    #Elimina los identificadores de pizza, su tipo e ingredientes
    df_master = df_master.drop(
        columns = ['pizza_id','pizza_type_id','ingredients']
    )

    #Concatena fecha y tiempo en una sola columna y se le convierte al tipo datetime
    df_master['order_timestamp'] = df_master['date'] + " " + df_master['time']
    df_master['order_timestamp'] = pd.to_datetime(df_master['order_timestamp'], errors= 'coerce')
    #Se elimina las columnas fecha y hora que se encontraban separadas
    df_master = df_master.drop(
        columns=['date','time']
    )

    #Cálculo del total de linea en base a la cantidad y precio
    df_master['total_line'] = df_master['quantity'] * df_master['price']

    #Ordena la tabla según la fecha y hora en ascendente.
    df_master = df_master.sort_values('order_timestamp')

    #Se crea un dataframe final de ventas con las columnas ordenadas para un mayor entendimiento
    columns_order = [
        'order_id', 'order_details_id', 'order_timestamp', 'name', 
        'category', 'size', 'quantity', 'price', 'total_line'
    ]
    df_pizza_sales = df_master[columns_order]

    return df_pizza_sales