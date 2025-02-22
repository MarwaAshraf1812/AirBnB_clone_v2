#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return FileStorage.__objects

        dic = dict()
        for key, value in FileStorage.__objects.items():
            if isinstance(value, cls):
                dic[key] = value
        return dic


    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(FileStorage.__file_path, 'r') as file:
                file_content = file.read()
                if file_content:
                    data = json.loads(file_content)
                    for key, value in data.items():
                        self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """Delete the object from objects"""
        if obj is not None:
            """Creates a unique key (my_obj) based on the object's class name and ID"""
            my_obj = obj.to_dict()['__class__'] + '.' + obj.id
            if my_obj in FileStorage.__objects:
                del FileStorage.__objects[my_obj]
                self.save()

    def close(self):
        """deserializing the JSON file to objects"""
        self.reload()
