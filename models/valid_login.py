#!/usr/bin/python3
"""
This is the ValidLogin class
"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, DateTime, ForeignKey
import models
from hashlib import md5
from datetime import datetime


class ValidLogin(BaseModel, Base):
  """
  ValidLogin class to track all valid logins
  """
  if models.storage_t == 'db':
    __tablename__ = 'valid_logins'
    user_name = Column(String(128), nullable=False)
    login_date = Column(DateTime, default=datetime.utcnow)
    consumer_id = Column(String(128), ForeignKey('consumers.id'))
  else:
      user_name = ""
      login_date = datetime.utcnow
      consuner_id = ""

  def __init__(self, *args, **kwargs):
      """
      Initializes a ValidLogin
      """
      super().__init__(*args, **kwargs)
