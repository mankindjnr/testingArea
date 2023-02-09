#!/usr/bin/env python3
"""
the creation of the class BaseModel
"""
from datetime import datetime, time, date
import uuid
from models import storage

class BaseModel:
    """
    the  class BaseModel with its public instances and method
    *args and **kwargs are optional arguments
    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """
        this is a string representation of the object
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    # public instance methods save and to_dict
    def save(self):
        """
        this updates th public instance attribute updated at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        a dictionary representation of the object with the keys __class__,
        created_at and updated at. the values of these keys are the values
        of the corresponding instance variables
        """
        dictionary = self.__dict__.copy()
        dictionary.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            })
        return dictionary
