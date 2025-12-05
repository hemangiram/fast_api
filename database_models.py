#/home/acquaint/fast_api/database_models.py
from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.ext.declarative  import declarative_base



Base = declarative_base()

class Product(Base):
    __tablename__="product"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
