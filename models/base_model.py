#!/usr/bin/env python3
"""
the creation of the class BaseModel
"""
from datetime import datetime, time, date
import uuid


class BaseModel:
    """
    the  class BaseModel with its public instances and method
    """
    def __init__(self, *args, **kwargs):
        """
        __init__ - >a class constructor  called when an object is created to
        initialize the attributes of the class.
        the following attr are oublic inst attri
        """
        if kwargs:
            """
            if kwargs is not empty each key of dictionary is an attribute name
            __class__, each value of this dictionary is the value of the attrr
            name
            create and update are strings, convert to datetime
            otherwise, if not kwargs create id and created at
            """
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
