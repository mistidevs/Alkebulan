#!/usr/bin/python3
"""This is the Consumers class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from hashlib import md5
import shlex


class Consumer(BaseModel, Base):
  """
  Consumer class for those purchasing farm produce
  """

  if models.storage_t == 'db':
    __tablename__ = 'consumers'
    user_name = Column(String(128), nullable=False)
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
  else:
      user_name = ""
      full_name = ""
      email = ""
      phone_number = ""

  def __init__(self, *args, **kwargs):
      """initializes a consumer"""
      super().__init__(*args, **kwargs)

  def __setattr__(self, name, value):
      """sets a password with md5 encryption"""
      if name == "password":
          value = md5(value.encode()).hexdigest()
      super().__setattr__(name, value)