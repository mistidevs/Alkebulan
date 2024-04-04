#!/usr/bin/python3
"""This is the Consumers class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from hashlib import md5
from flask_login import UserMixin
import shlex


class Consumer(BaseModel, UserMixin, Base):
  """
  Consumer class for those purchasing farm produce
  """

  import models
  if models.storage_t == 'db':
    __tablename__ = 'consumers'
    picture = Column(String(128), default="/defaults/default_consumer.jpg")
    user_name = Column(String(128), nullable=False)
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
  else:
      picture = "/defaults/default_consumer.jpg"
      user_name = ""
      full_name = ""
      email = ""
      phone_number = ""
      password = ""

  def __init__(self, *args, **kwargs):
      """initializes a consumer"""
      super().__init__(*args, **kwargs)

  def __setattr__(self, name, value):
      """sets a password with md5 encryption"""
      if name == "password":
          value = md5(value.encode()).hexdigest()
      super().__setattr__(name, value)