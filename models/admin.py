#!/usr/bin/python3
"""This is the Administrators class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from hashlib import md5
import shlex


class Admin(BaseModel, Base):
  """
  Admin class that allows management of the system
  """

  if models.storage_t == 'db':
    __tablename__ = 'admins'
    user_name = Column(String(128), nullable=False)
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
  else:
      user_name = ""
      full_name = ""
      email = ""

  def __init__(self, *args, **kwargs):
      """initializes an administrator"""
      super().__init__(*args, **kwargs)

  def __setattr__(self, name, value):
      """sets a password with md5 encryption"""
      if name == "password":
          value = md5(value.encode()).hexdigest()
      super().__setattr__(name, value)