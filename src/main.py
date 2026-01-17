from database import engine
from models import Base
from etl_logic import *


def run_pipeline():
    
    #Elimina tablas existentes
    Base.metadata.drop_all(engine)

    #Crea tablas
    Base.metadata.create_all(engine)

    #Extrae datos de las ordenes
    raw_orders = get_orders_raw_data()

    #Extrae datos del detalle de las ordenes
    raw_orders_detail = get_orders_detail_raw_data()

    #Extrae informacion de la pizza
    raw_pizzas = get_pizzas_raw_data()

    #Extrae descripcion de la pizza
    raw_pizza_details = get_pizzas_types_raw_data()

    #Trae la sabana de datos sin normalizar
    raw_master = build_analytical_orders_data(
        raw_orders= raw_orders,
        raw_order_details= raw_orders_detail,
        raw_pizza= raw_pizzas,
        raw_pizza_types= raw_pizza_details
    )

    #Transforma y normaliza la sabana de datos
    pizza_orders_data = transform_and_format_orders_data(raw_master)

    #Carga los datos correspondientes a la tabla sql
    pizza_orders_data.to_sql(name='orders', con=engine, if_exists='append', index=False)


if __name__ == '__main__':
    run_pipeline()