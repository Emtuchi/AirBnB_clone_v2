#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

storage_type = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if storage_type == "db":
        reviews = relationship('Review', cascade="all,delete", backref="place")
    else:
        @property
        def reviews(self):
            """Getter document"""
            reviewsList = []
            reviewsAll = models.storage.all(Review)
            for review in reviewsAll.values():
                if review.place_id in self.id:
                    reviewsList.append(review)
            return reviewsList
