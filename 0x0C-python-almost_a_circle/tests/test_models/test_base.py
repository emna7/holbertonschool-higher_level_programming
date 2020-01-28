#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_Increment(self):
        """ tests creating a new obj increments
        nb_objects
        """
        base = Base()
        self.assertEqual(base.id, base._Base__nb_objects)
        base2 = Base()
        self.assertEqual(base2.id, base2._Base__nb_objects)
    def test_IdIsString(self):
        """ tests id as string
        """
        basestr = Base("String")
        self.assertEqual(basestr.id, "String")
