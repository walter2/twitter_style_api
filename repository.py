#!/user/bin/python3
# encoding: utf-8

"""
repository.py represents the data story for the twitter like api program.
"""


from user import User


class Repository:
    """ Repository models the data story for the twitter like application.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, first_name, last_name, user_name, password):
        """ register() takes a first last and user name and a password.
        A new user is created and added to self.users.
        The function returns True. 
        """
        self.users[user_name] = User(first_name, last_name, user_name, password)
        return True
