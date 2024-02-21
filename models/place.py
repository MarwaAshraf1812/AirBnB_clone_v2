#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.review import Review
import os
from os import environ

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))

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
    if environ.get('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', secondary='place_amenity',
                             back_populates='place_amenities', overlaps="amenities")

    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def reviews(self):
            """Getter Place's Reviews"""
            from models import storage
            # Get all Review instances from the storage
            review_instances = storage.all(Review)
            # Filter reviews based on the place_id
            return [review for review in review_instances.values() if review.place_id == self.id]


        @property
        def amenities(self):
            """Getter for Place's Amenities"""
            from models import storage
            from models.amenity import Amenity
            amenity_instances = storage.all(Amenity)
            return [amenity for amenity in amenity_instances.values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Setter for Place's Amenities"""
            from models.amenity import Amenity
            if obj and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
