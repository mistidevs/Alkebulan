#!/usr/bin/python3
"""
This is the InvalidLogin class
"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, DateTime
import models
from hashlib import md5
from datetime import datetime


class InvalidLogin(BaseModel, Base):
  """
  InvalidLogin class to track all valid logins
  """
  if models.storage_t == 'db':
    __tablename__ = 'invalid_logins'
    user_name = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    reason = Column(String(128), nullable=False)
    login_date = Column(DateTime, default=datetime.utcnow)
  else:
      user_name = ""
      password = ""
      reason = ""
      login_date = datetime.utcnow

  def __init__(self, *args, **kwargs):
      """
      Initializes an InvalidLogin
      """
      super().__init__(*args, **kwargs)
