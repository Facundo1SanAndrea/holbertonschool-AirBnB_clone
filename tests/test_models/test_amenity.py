#!/usr/bin/python3
"""Tests for base class amenity """
import unittest
from models.amenity import Amenity


class Testuser(unittest.TestCase):
    ''' unittest class for checking amenity'''

    def test_create_place(self):
        ''' creating amenity class '''
        amenity1 = Amenity()
        self.assertEqual(amenity1.name, "")

if __name__ == '__main__':
    unittest.main()