#!/user/bin/python3
# encoding: utf-8

"""
service_api.py implements the API through which interactions are done
with the twitter like program.
"""

from repository import Repository


class Service:
    """ Service is the API through which the twitter like application is 
     accessed.
     At the initiation a repository is required.
    """

    def __init__(self, repository):
        self.repository = repository

    def register_user(self, first_name, last_name, user_name, password):
        """register() takes the first name, last name, user name and password
        of a new user.
        It returns True if a new user is successfully registered.
        """
        self.repository.register_user(
            first_name,
            last_name,
            user_name,
            password
            )
        return True

    def get_users(self):
        """ get_users() returns the currently registered self.users list."""
        users = [key for key in self.repository.users.keys()]
        return users
