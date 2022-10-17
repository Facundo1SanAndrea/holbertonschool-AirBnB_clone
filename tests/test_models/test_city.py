
"""Tests for base class city """
import unittest
from models.city import City


class Testuser(unittest.TestCase):
    ''' unittest class for checking city'''

    def test_create_state(self):
        ''' creating city class '''
        state1 = City()
        self.assertEqual(state1.state_id, "")
        self.assertEqual(state1.name, "")

if __name__ == '__main__':
    unittest.main()