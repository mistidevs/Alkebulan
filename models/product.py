#!/usr/bin/python3
"""This is the Products class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex


class Product(BaseModel, Base):
  """
  Products class holding products being sold
  """

  if models.storage_t == 'db':
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    recommended_price = Column(Integer, nullable=False)
    max_price = Column(Integer, nullable=False)
    min_price = Column(Integer, nullable=False)
    description = Column(String(1024), nullable=False)
  else:
      name = ""
      recommended_price = 0
      max_price = 0
      min_price = 0
      description = ""

  def __init__(self, *args, **kwargs):
      """initializes an administrator"""
      super().__init__(*args, **kwargs)