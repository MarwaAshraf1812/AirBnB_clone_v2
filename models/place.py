#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.review import Review
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')


    # For FileStorage
    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Getter Place's Reviews"""
            from models import storage
            # Get all Review instances from the storage
            review_instances = storage.all(Review)
            # Filter reviews based on the place_id
            return [review for review in review_instances.values() if review.place_id == self.id]
