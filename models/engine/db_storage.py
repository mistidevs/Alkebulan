#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.admin import Admin
from models.consumer import Consumer
from models.farmer_product import FarmerProduct
from models.farmer import Farmer
from models.order import Order
from models.product import Product
from models.valid_login import ValidLogin
from models.invalid_login import InvalidLogin
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Admin": Admin, "Consumer": Consumer, 
           "FarmerProduct": FarmerProduct, "Farmer": Farmer,
           "Product": Product, "Order": Order,
           "ValidLogin": ValidLogin, "InvalidLogin": InvalidLogin}


class DBStorage:
    """
    Interaacts with the MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate a DBStorage object
        """
        ALKEBULAN_MYSQL_USER = getenv('ALKEBULAN_MYSQL_USER')
        ALKEBULAN_MYSQL_PWD = getenv('ALKEBULAN_MYSQL_PWD')
        ALKEBULAN_MYSQL_HOST = getenv('ALKEBULAN_MYSQL_HOST')
        ALKEBULAN_MYSQL_DB = getenv('ALKEBULAN_MYSQL_DB')
        ALKEBULAN_ENV = getenv('ALKEBULAN_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ALKEBULAN_MYSQL_USER,
                                             ALKEBULAN_MYSQL_PWD,
                                             ALKEBULAN_MYSQL_HOST,
                                             ALKEBULAN_MYSQL_DB))
        if ALKEBULAN_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Yield all objects or objects of a specific class
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads data from the database
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        Call remove() method on the private session attribute
        restarting the database session with any new changes
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
