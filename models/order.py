#!/usr/bin/python
""" holds class FarmerProduct"""
import models
from datetime import datetime
import random
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean


class Order(BaseModel, Base):
    """Representation of Order """
    if models.storage_t == 'db':
        __tablename__ = 'farmer_product'
        farmer_product_id = Column(String(60), ForeignKey('farmer_products.id'), nullable=False)
        consumer_id = Column(String(60), ForeignKey('consumers.id'), nullable=False)
        price = Column(String(60), ForeignKey('farmer_products.price'), nullable=False)
        quantity = Column(Integer, nullable=False)
        order_date = Column(DateTime, default=datetime.utcnow)
        order_verification_pin = Column(Integer, default=lambda: random.randint(100000, 999999))
        completed = Column(Boolean, default=False)
    else:
        farmer_product_id = ""
        consumer_id = ""
        price = 0
        quantity = 0
        order_date = datetime.utcnow
        order_verification_pin = lambda: random.randint(100000, 999999)
        completed = False

    def __init__(self, *args, **kwargs):
        """initializes Order"""
        super().__init__(*args, **kwargs)
