#!/user/bin/python3
# encoding: utf-8

"""
Tests for the service api.
"""

import unittest
from repository import Repository
from service_api import Service

class TestService(unittest.TestCase):
    """Tests the functionallity of the service api."""

    def test_new_service_requiers_repository(self):
        repository = Repository()
        service = Service(repository)
        expected = True
        actual = isinstance(service, Service)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
