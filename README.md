# Proyecto de automatización de carga de pedidos en una pizzería.

El presente proyecto consiste en la automatización en el proceso de carga de órdenes registradas de una pizzeria a una base de datos.

## 📋 Contenido

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura](#estructura)

## ✨ Características

- Detección automática del formato de encoding de los archivos fuentes.
- Extracción de datos desde múltiple fuentes de archivos csv
- Consolidación de datos en una sola sábana de información.
- Limpieza y normalización de datos para un mejor entendimiento.
- Inclusión de proceso de logging para la determinar en qué punto se encuentra el proceso de carga.
- Conexión segura hacia la base de datos SQL.
- Generación del modelo de datos personalizado mediante ORM de SQL Alchemy.
- Control de errores ante cualquier eventualidad.

## 📦 Requisitos

- Python 3.8+
- SQL Server 2016+
- ODBC Driver for SQL Server

## 🚀 Instalación

```bash
git clone https://github.com/juanacvm/PizzaOrders.git
cd PizzaOrders

# Creación del entorno virtual de pruebas
python -m venv venv
venv\Scripts\activate  # Windows

# Instalación de dependencias (librerías)
pip install -r requirements.txt
```

## ⚙️ Configuración

Modificar el archivo `.env.example` a `.env`

Añadir tus parámetros a  `.env` con los parámetros de SQL Server:

```python
db_server = "Nombre de tu servidor"
db_name = "Nombre de base de datos"
db_user = "Usuario de acceso a la base de datos"
db_password = "Contraseña del usuario"
db_driver = "Nombre del driver, puede ser ODBC Driver 17 for SQL Server"
```

Verificar que los archivos CSV existan en la carpeta `data/`:
- `orders.csv`
- `order_details.csv`
- `pizzas.csv`
- `pizza_types.csv`

## 🔧 Uso

```bash
cd src
python main.py
```

## 📁 Estructura

```
PizzaOrders/
├── README.md
├── requirements.txt
├── data/                    # Carpeta que aloja los archivos CSV
│   ├── orders.csv
│   ├── order_details.csv
│   ├── pizzas.csv
│   └── pizza_types.csv
├── src/                     # Carpeta de código fuente
│   ├── config.py           # Configuración de variables .env
│   ├── database.py         # Conexión a BD
│   ├── models.py           # Diseño de modelos ORM
│   ├── etl_logic.py        # Lógica ETL
│   └── main.py             # Punto de ejecución de pipeline
└── notebooks/
    └── script.ipynb        # Notebook de pruebas del procesamiento de datos.
```

## 📊 Tabla de Salida

**Tabla: orders (SQL Server)**

- **order_id**: Número de identificador del pedido
- **order_details_id (PK)**: Número del detalle de pedido
- **order_timestamp**: Fecha y hora del pedido
- **name**: Nombre de pizza
- **category**: Categoría de la pizza
- **size**: Tamaño de la pizza
- **quantity**: Cantidad de pizzas solicitadas
- **price**: Precio por unidad
- **total_line**: Precio total del detalle

## 👤 Autor

[Juan](https://github.com/juanacvm)

---

**Última actualización**: 19 de Enero 2026