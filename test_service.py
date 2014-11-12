#!/user/bin/python3
# encoding: utf-8

"""
Tests for the service api.
"""


import unittest

from repository import Repository
from service_api import Service
from user import User


class TestService(unittest.TestCase):
    """Tests the functionallity of the service api."""

    def setUp(self):
        self.repository = Repository()
        self.service = Service(self.repository)

# service start

    def test_new_service_requiers_repository(self):
        repository = Repository()
        service = Service(repository)
        expected = True
        actual = isinstance(service, Service)
        self.assertEqual(expected, actual)

# user registration

    def test_new_user_can_be_registered_through_service(self):
        actual = self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.assertTrue(actual)

    def test_a_user_name_can_be_only_registered_once(self):        
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = 'The user \'bhill\' exists already. Please choose another user name.'
        actual = self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.assertEqual(expected, actual)

    def test_user_registration_requiers_first_name(self):
        with self.assertRaises(ValueError):
            self.service.register_user('', 'Hill', 'bhill', 'qwerty')

    def test_user_registration_requiers_last_name(self):
        with self.assertRaises(ValueError):
            self.service.register_user('Bill', '', 'bhill', 'qwerty')

    def test_user_registration_requiers_user_name(self):
        with self.assertRaises(ValueError):
            self.service.register_user('Bill', 'Hill', '', 'qwerty')

    def test_user_registration_requiers_password(self):
        with self.assertRaises(ValueError):
            self.service.register_user('Bill', 'Hill', 'bhill', '')
# user display
    def test_service_has_access_to_existing_users(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = ['bhill']
        actual = self.service.get_users()
        self.assertEqual(expected, actual)
        self.assertTrue(isinstance(self.service.repository.users['bhill'], User)
)

# user login

    def test_user_can_login_with_matching_details(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = True
        actual = self.service.login('bhill', 'qwerty')
        self.assertEqual(expected, actual)
    
    def test_user_cannot_login_with_false_password(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = False
        actual = self.service.login('bhill', 'incorrect')
        self.assertEqual(expected, actual)

    def test_user_cannot_login_with_incorrect_user_name(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = False
        actual = self.service.login('bmount', 'qwerty')
        self.assertEqual(expected, actual)

# user logout

    def test_a_logged_in_user_can_logout(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.login('bhill', 'qwerty')
        expected = True
        actual = self.service.logout('bhill')
        self.assertEqual(expected, actual)

    def test_only_logged_in_users_can_be_logged_out(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.register_user('Tim', 'House', 'thouse', 'pass')
        self.service.login('bhill', 'qwerty')
        expected = False
        actual = self.service.logout('thouse')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
