#!/usr/bin/python3
"""
this is the module base
"""
import json


class Base():
    """ Base keeps track of the number of objects
    Attributes:
        nb_objects (obj:`int`): private - number of objects
        id (obj:`int`): public - id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ the to_json function """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ the save file function """
        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
        with open(cls.__name__ + '.json', mode='w+',
                  encoding='utf-8') as a_file:
            a_file.write(json_string)

    def from_json_string(json_string):
        """ from json function """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return(json.loads(json_string))
