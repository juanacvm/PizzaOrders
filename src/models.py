from sqlalchemy import Column 
from sqlalchemy.types import Integer, Float, NVARCHAR, DateTime
from sqlalchemy.orm import declarative_base 

Base = declarative_base()

#Crea la tabla de Ordenes de Pizza
class Sales(Base):
    __tablename__ = 'orders'

    order_id = Column(NVARCHAR(40))
    order_details_id = Column(NVARCHAR(40),primary_key=True, autoincrement=False)
    order_timestamp = Column(DateTime)
    name = Column(NVARCHAR(100))
    category = Column(NVARCHAR(100))
    size = Column(NVARCHAR(5))
    quantity = Column(Integer)
    price = Column(Float)
    total_line = Column(Float)