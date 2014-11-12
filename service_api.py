#!/user/bin/python3
# encoding: utf-8

"""
service_api.py implements the API through which interactions are done
with the twitter like program.
"""

from repository import Repository
from user import User


class Service:
    """ Service is the API through which the twitter like application is 
     accessed.
     At the initiation a repository is required.
    """

    def __init__(self, repository):
        self.repository = repository
        self.users = {}

    def register_user(self, first_name, last_name, user_name, password):
        """register() takes the first name, last name, user name and password
        of a new user.
        It returns True if a new user is successfully registered.
        """
        new_user = User(first_name, last_name, user_name, password)
        self.users[str(new_user)] = new_user
        return True

    def get_users(self):
        """ get_users() returns the currently registered self.users list."""
        users = [key for key in self.users.keys()]
        return users
