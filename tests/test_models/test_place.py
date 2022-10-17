"""Tests for base class place """
import unittest
from models.place import Place


class Testuser(unittest.TestCase):
    ''' unittest class for checking place'''

    def test_create_place(self):
        ''' creating place class '''
        place1 = Place()
        self.assertEqual(place1.city_id, "")
        self.assertEqual(place1.user_id, "")
        self.assertEqual(place1.name, "")
        self.assertEqual(place1.description, "")
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()