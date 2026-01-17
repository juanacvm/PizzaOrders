import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('DB_SERVER')
db_name = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_driver = os.getenv('DB_DRIVER')