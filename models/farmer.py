#!/usr/bin/python3
"""This is the Farmers class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, String
import models
from hashlib import md5
import shlex


class Farmer(BaseModel, Base):
  """
  Farmers class for people selling fresh produce
  """

  if models.storage_t == 'db':
    __tablename__ = 'farmers'
    user_name = Column(String(128), nullable=False)
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
    location = Column(String(128), nullable=False)
    latitude = Column(Float(precision=8), nullable=False)
    longitude = Column(Float(precision=8), nullable=False) 
  else:
      user_name = ""
      full_name = ""
      email = ""
      phone_number = ""
      location = ""
      latitude = 0.0
      longitude = 0.0

  def __init__(self, *args, **kwargs):
      """initializes a farmer"""
      super().__init__(*args, **kwargs)

  def __setattr__(self, name, value):
      """sets a password with md5 encryption"""
      if name == "password":
          value = md5(value.encode()).hexdigest()
      super().__setattr__(name, value)