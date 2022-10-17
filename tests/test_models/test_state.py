
"""Tests for base class state """
import unittest
from models.state import State


class Testuser(unittest.TestCase):
    ''' unittest class for checking state'''

    def test_create_state(self):
        ''' creating state class '''
        state1 = State()
        self.assertEqual(state1.name, "")

if __name__ == '__main__':
    unittest.main()