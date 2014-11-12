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

    def test_new_service_requiers_repository(self):
        repository = Repository()
        service = Service(repository)
        expected = True
        actual = isinstance(service, Service)
        self.assertEqual(expected, actual)

    def test_new_user_can_be_registered_through_service(self):
        actual = self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        self.assertTrue(actual)

    def test_service_has_access_to_existing_users(self):
        self.service.register_user('Bill', 'Hill', 'bhill', 'qwerty')
        expected = ['bhill']
        actual = self.service.get_users()
        self.assertEqual(expected, actual)
        self.assertTrue(isinstance(self.service.users['bhill'], User))


if __name__ == '__main__':
    unittest.main(exit=False)
