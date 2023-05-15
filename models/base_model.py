#!/usr/bin/python3
"""module for BaseModel
   contains the AirBnB base class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class, object hierachy"""

    def __init__(self, *args, **kwargs):
        """initializes instances of our class base model

        Args:
            *args: list of arguments
            **kwargs: dict containing key value arguments
        """

        if kwargs is not none and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)

    def __str__(self):
        """returns string representation of an instance"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """represents an instance as a dictionary"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return (my_dict)
