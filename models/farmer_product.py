#!/usr/bin/python
""" holds class FarmerProduct"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String


class FarmerProduct(BaseModel, Base):
    """Representation of FarmerProduct """
    if models.storage_t == 'db':
        __tablename__ = 'farmer_products'
        farmer_id = Column(String(60), ForeignKey('farmers.id'), nullable=False)
        product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
        price = Column(Integer, nullable=False)
    else:
        picture = ""
        farmer_id = ""
        product_id = ""
        price = 0

    def __init__(self, *args, **kwargs):
        """initializes FarmerProduct"""
        super().__init__(*args, **kwargs)
