#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
import random


class Order(BaseModel, Base):
    """
    Order class for recording consumer orders on farmer products
    """

    if models.storage_t == 'db':
        __tablename__ = 'orders'
        consumer_id = Column(String(60), ForeignKey('consumers.id'), nullable=False)
        farmer_id = Column(String(60), ForeignKey('farmers.id'), nullable=False)
        product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
        order_date = Column(DateTime, default=datetime.utcnow)
        order_verification_pin = Column(Integer, default=lambda: random.randint(100000, 999999))
        completed = Column(Boolean, default=False)
        in_cart = Column(Boolean, default=True)
        quantity = Column(Integer, nullable=False)
        unit_price = Column(Integer, nullable=False)
        total_price = Column(Integer, nullable=False)
        farmer_review = Column(String(1024), nullable=True)
        consumer_review = Column(String(1024), nullable=True)
    else:
        picture = ""
        consumer_id = ""
        farmer_id = ""
        product_id = ""
        order_date = datetime.utcnow
        unit_price = 0
        quantity = 0
        total_price = 0
        order_verification_pin = lambda: random.randint(100000, 999999)
        completed = False
        in_cart = True
        farmer_review = ""
        consumer_review = ""

    def __init__(self, *args, **kwargs):
        """Initializes an order"""
        super().__init__(*args, **kwargs)
