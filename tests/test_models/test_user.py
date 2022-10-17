"""Tests for base class User """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    ''' unittest class for checking User'''

    def test_create_user(self):
        ''' creating user class '''
        user1 = User()
        self.assertEqual(user1.email, "")
        self.assertEqual(user1.password, "")
        self.assertEqual(user1.first_name, "")
        self.assertEqual(user1.last_name, "")

if __name__ == '__main__':
    unittest.main()