import logging
import time
import sys
from database import engine_master,create_database,sql_query
from models import Base
from etl_logic import *

#Configuracion basica de log
logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Se crea log
log = logging.getLogger(__name__)


def run_pipeline():
    
    log.info('Iniciando pipeline de datos...')
    time.sleep(40)

    try:

        log.info('Creando la base de datos en caso no exista...')
        create_database(engine_master, sql_query)

        log.info('Eliminando tablas existentes...')
        #Elimina tablas existentes
        Base.metadata.drop_all(engine_master)

        log.info('Creando tablas en la base de datos...')
        #Crea tablas
        Base.metadata.create_all(engine_master)


        log.info('Extrayendo los datos relacionados a los pedidos de pizza...')
        #Extrae datos de las ordenes
        raw_orders = get_orders_raw_data()

        log.info('Extrayendo los datos detallados relacionados a los pedidos de pizza...')
        #Extrae datos del detalle de las ordenes
        raw_orders_detail = get_orders_detail_raw_data()

        log.info('Extrayendo los datos relacionados a las pizzas...')
        #Extrae informacion de la pizza
        raw_pizzas = get_pizzas_raw_data()

        log.info('Extrayendo los datos relacionados a la descripcion detallada de las pizzas...')
        #Extrae descripcion de la pizza
        raw_pizza_details = get_pizzas_types_raw_data()

        log.info('Creando la sabana de datos general de pedidos...')  
        #Trae la sabana de datos sin normalizar
        raw_master = build_analytical_orders_data(
            raw_orders= raw_orders,
            raw_order_details= raw_orders_detail,
            raw_pizza= raw_pizzas,
            raw_pizza_types= raw_pizza_details
        )

        log.info('Transformando y normalizando los datos...')
        #Transforma y normaliza la sabana de datos
        pizza_orders_data = transform_and_format_orders_data(raw_master)

        log.info('Cargando los datos a la tabla de pedidos...')
        #Carga los datos correspondientes a la tabla sql
        pizza_orders_data.to_sql(name='orders', con=engine_master, if_exists='append', index=False)

        log.info('Se ha culminado con la carga del pipeline de pedidos de pizza...')

    except FileNotFoundError as e:
        log.error(f"No se ha podido cargar los documentos de datos: {e}")
        sys.exit(1)

    except ValueError as e:
        log.error(f"Hubo error con el procesamiento de datos {e}")
        sys.exit(1)

    except Exception as e:
        log.error(f"El proceso de pipeline se detuvo debido a un error inesperado {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_pipeline()