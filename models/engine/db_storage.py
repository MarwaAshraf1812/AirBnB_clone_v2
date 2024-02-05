#!/usr/bin/python3
"""This module defines a class to manage file DB storage for hbnb clone"""

from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity



class DBStorage:
    """ClassDBStorage is used to store and retrieve data from the database."""
    __engine = None
    __session = None
    def __init__(self):
        """"""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(username,
                                                            password,
                                                            host,
                                                            db_name)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in DB storage"""
        dic = {}
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
            for model in classes:
                for obj in self.__session.query(model).all():
                    obj_key = "{}.{}".format(type(obj).__name__, obj.id)
                    dic[obj_key] = obj
        else:
            if type(cls) is str:
                cls = eval(cls)
            for obj in self.__session.query(cls):
                obj_key = "{}.{}".format(type(obj).__name__, obj.id)
                dic[obj_key] = obj

        return (dic)

    def new(self, obj):
        """add the object to the current database session"""
        from sqlalchemy.orm import make_transient
        if not obj._sa_instance_state.session_id:
            self.__session.add(obj)
        else:
            # Expire the object to detach it from the current session
            make_transient(obj)
            self.__session.add(obj)

    def save(self):
        """commit the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all objects in the current database session"""
        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine,
                                 autocommit=False,
                                 expire_on_commit=False)
        session= scoped_session(session_f)
        self.__session = session()

    def close(self):
        """close the current database connection"""
        self.__session.close()
