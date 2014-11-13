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
        with self.assertRaises(ValueError):
            self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')

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

# user login

    def test_user_can_login_with_matching_details(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = True
        actual = self.service.login('bhill', 'qwerty')
        self.assertTrue(actual)
    
    def test_user_cannot_login_with_false_password(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        with self.assertRaises(ValueError):
            self.service.login('bhill', 'incorrect')

    def test_user_cannot_login_with_incorrect_user_name(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        with self.assertRaises(ValueError):
            self.service.login('billh', 'qwerty')

    def test_logged_in_user_gets_a_token_assigned(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        token = self.service.login('bhill', 'qwerty')
        expected = 'bhill'
        actual = token.user_name
        self.assertEqual(expected, actual)

    def test_multiple_users_can_login_to_the_service(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.register_user('Tim', 'House', 'thouse', 'pass')
        self.service.login('bhill', 'qwerty')
        self.service.login('thouse', 'pass')
        expected = 2
        actual = len(self.repository.tokens)
        self.assertEqual(expected, actual)

# user logout

    def test_a_logged_in_user_can_logout(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        token = self.service.login('bhill', 'qwerty')
        expected = True
        actual = self.service.logout('bhill')
        self.assertEqual(expected, actual)
        self.assertFalse(token in self.repository.tokens)

    def test_only_logged_in_users_can_be_logged_out(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.register_user('Tim', 'House', 'thouse', 'pass')
        self.service.login('bhill', 'qwerty')
        with self.assertRaises(ValueError):
            self.service.logout('thouse')

# user post creation

    def test_logged_in_user_can_post(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        token = self.service.login('bhill', 'qwerty')
        self.service.post(token, 'this is my post')
        expected = ['this is my post']
        actual = self.repository.get_public_time_line('bhill')
        self.assertEqual(expected, actual)

    def test_logged_out_user_cannot_post(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        token = 'abcdef'
        with self.assertRaises(ValueError):
            self.service.post(token, 'this is my post')

# followint users

    def test_logged_in_user_can_follow_other_users(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.register_user('Ann', 'White', 'awhite', 'secret')
        self.service.register_user('Tim', 'House', 'thouse', 'pass')
        token = self.service.login('bhill', 'qwerty')
        self.service.follow(token, 'awhite')
        self.service.follow(token, 'thouse')
        expected = ['awhite', 'thouse']
        actual = self.repository.users['bhill'].following
        self.assertEqual(expected, actual)

    def test_logged_in_user_cannot_follow_another_user_twice(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.register_user('Ann', 'White', 'awhite', 'secret')
        self.service.register_user('Tim', 'House', 'thouse', 'pass')
        token = self.service.login('bhill', 'qwerty')
        self.service.follow(token, 'awhite')
        self.service.follow(token, 'thouse')
        with self.assertRaises(ValueError):
            self.service.follow(token, 'thouse')

    def test_logged_in_user_cannot_follow_non_existing_user(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.service.register_user('Ann', 'White', 'awhite', 'secret')
        token = self.service.login('bhill', 'qwerty')
        self.service.follow(token, 'awhite')
        with self.assertRaises(ValueError):
            self.service.follow(token, 'not_here')

if __name__ == '__main__':
    unittest.main(exit=False)
