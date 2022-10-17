"""Tests for base class review """
import unittest
from models.review import Review


class Testuser(unittest.TestCase):
    ''' unittest class for checking review'''

    def test_create_place(self):
        ''' creating review class '''
        review1 = Review()
        self.assertEqual(review1.place_id, "")
        self.assertEqual(review1.user_id, "")
        self.assertEqual(review1.text, "")

if __name__ == '__main__':
    unittest.main()