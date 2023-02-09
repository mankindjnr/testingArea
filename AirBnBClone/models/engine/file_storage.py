#!/usr/bin/env python3
"""
a class filestorage that serializes instances to json file and deserializes
json file instances
"""


import json

class FileStorage:
    """
    the serialization and deserialization class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the object
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in objects obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file(path ___path)
        """
        dictionary = {}
        for key, value in FileStorage.__objects.items():
                dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:

            json.dump(dictionary, f)

    def reload(self):
        """
        deserializes the json file to __objects only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t
        exist, no exceptions should be raised.
        """
        from models.base_model import BaseModel

        class_dict = {"BaseModel": BaseModel}
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
                FileStorage.__objets = obj
        except FileNotFoundError:
            pass
