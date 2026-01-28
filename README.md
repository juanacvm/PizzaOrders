# Pipeline ETL para la carga de pedidos de pizza con Pandas, SQLAlchemy y Docker

## Descripción

Proyecto que implementa un pipeline de extracción, transformación y carga (ETL) utilizando Python. Consume datos de múltiples archivos CSV relacionados con órdenes e información de pizzas, transforma los datos a través de pandas y los guarda en una tabla SQL creada mediante SQLAlchemy. Además de ello, aplica control de errores durante el proceso de la implementación.

## Características

- **Separación de responsabilidades:** Creación de métodos en distintos archivos `.py` para separar la lógica de configuración, conexión a base de datos, transformación de datos y ejecución del pipeline, logrando un mejor mantenimiento del código.

- **Extracción dinámica:** Implementación de lectura inteligente de múltiples archivos CSV desde la carpeta de datos (órdenes, detalles de órdenes, pizzas y tipos de pizzas) para evitar rutas hardcodeadas.

- **Seguridad:** Gestión de credenciales mediante variables de entorno `.env` para separar información sensible con el código fuente.

- **Logging:** Sistema de logs con niveles de severidad (INFO, ERROR, DEBUG) para gestión completa de trazabilidad del pipeline.

- **Integración a Docker:** Creación de contenedores aislados para garantizar la ejecución del pipeline desde cualquier entorno sin dependencias del sistema.

## Arquitectura del Pipeline

El pipeline sigue el procedimiento ETL estándar:

```
Entrada (Múltiples CSV) → Extracción → Transformación → Carga (SQL Server)
```

### Flujo de datos:

1. **Extracción**: Lee datos de cuatro archivos CSV:
   - `orders.csv` - Información general del pedido
   - `order_details.csv` - Detalle del pedido
   - `pizzas.csv` - Catálogo de pizzas disponibles
   - `pizza_types.csv` - Categorías de las pizzas

2. **Transformación**: 
   - Fusión de múltiples fuentes de datos
   - Normalización de columnas
   - Conversión de tipos de datos
   - Limpieza de valores nulos
   - Enriquecimiento de datos con información relacional
   - Relleno de valores faltantes según tipo de dato

3. **Carga**: Carga de datos consolidados en tabla SQL Server

## Tecnologías Utilizadas

- **Python 3.11**
- **Pandas**: Para la carga y transformación de datos
- **SQLAlchemy**: Para la gestión de base de datos (ORM)
- **python-dotenv**: Para la configuración de variables de entorno
- **Docker**: Para la creación de los contenedores del proyecto
- **SQL Server 2022**: Para la gestión de base de datos relacionales

## Estructura del Proyecto

```
PizzaOrders/
├── data/
│   ├── order_details.csv               # Detalle por pedido
│   ├── orders.csv                      # Información de pedidos
│   ├── pizza_types.csv                 # Tipos y categorías de pizzas
│   └── pizzas.csv                      # Catálogo de pizzas
├── notebooks/
│   └── script.ipynb                    # Notebook de pruebas
├── src/
│   ├── main.py                         # Script principal del pipeline
│   ├── config.py                       # Configuración de variables de entorno
│   ├── database.py                     # Conexión y gestión de base de datos
│   ├── models.py                       # Creación de modelos ORM de tablas
│   └── etl_logic.py                    # Lógica de extracción y transformación
├── Dockerfile                          # Configuración de contenedor
├── docker-compose.yaml                 # Orquestación de servicios
├── requirements.txt                    # Dependencias de Python
├── .gitignore                          # Archivos ignorados por Git
└── README.md                           # Este archivo
```

## Prerequisitos

- Python 3.11 o superior
- SQL Server 2019 o superior instalado
- Git para clonar el repositorio
- Docker y Docker Compose (opcional, para ejecución en contenedores)
- Acceso a línea de comandos (PowerShell, CMD o Terminal)
- pip (Gestor de paquetes de Python)

## Configuración e Instalación

### Opción 1: Ejecución a nivel local

#### Requisitos previos:
- Python 3.11+
- SQL Server en ejecución
- pip (gestor de paquetes)

#### Instalación:

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Configurar variables de entorno (reemplazar `.env.example` por `.env`):**
```
DB_SERVER="Nombre del servidor (SELECT @@SERVERNAME)"
DB_NAME="Nombre de la base de datos"
DB_USER="Usuario de base de datos"
DB_PASSWORD="Contraseña del usuario de base de datos"
DB_DRIVER="Driver de DB, puede ser: ODBC Driver 17 for SQL Server"
```

3. **Ejecutar el pipeline:**
```bash
python src/main.py
```

### Opción 2: Ejecución con Docker

#### Requisitos:
- Docker y Docker Compose instalados

#### Instalación:

1. **Configurar variables de entorno (reemplazar `.env.example` por `.env`):**
```
DB_SERVER=mssql_pizza_server,1433
DB_NAME="Nombre de la base de datos"
DB_USER=sa
DB_PASSWORD="Contraseña del usuario de base de datos"
DB_DRIVER=ODBC Driver 17 for SQL Server
```

2. **Construir e iniciar los contenedores:**
```bash
docker-compose up --build
```

3. **Detener los servicios:**
```bash
docker-compose down
```

#### Configuración de Docker:
- SQL Server se ejecuta en puerto `1434` (mapeo desde 1433 interno)
- Python se inicia automáticamente tras la disponibilidad de SQL Server
- Los datos se persisten en volumen `mssql_data`

> **Nota:** El proyecto requiere las librerías especificadas en `requirements.txt`. Todas se instalan automáticamente al ejecutar `pip install -r requirements.txt` en la opción local, o se incluyen en la imagen Docker para la opción de contenedores.