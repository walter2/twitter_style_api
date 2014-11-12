#!/user/bin/python3
# encoding: utf-8

"""
user.py contains the user class for the twitter like api program.
"""



class User:
    """ Class User represents a user in the program.
    """

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def __str__(self):
        """String repesentation of user with the user_name."""
        return self.user_name
