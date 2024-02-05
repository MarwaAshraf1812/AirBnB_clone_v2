#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ =  "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')


    # For FileStorage
    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Getter attribute for cities"""
            from models import storage
            city_instances = storage.all(City)
            return [city for city in city_instances.values() if city.state_id == self.id]
