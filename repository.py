#!/user/bin/python3
# encoding: utf-8

"""
repository.py represents the data story for the twitter like api program.
"""


import random

from session_token import Token
from user import User


class Repository:
    """ Repository models the data story for the twitter like application.
    """

    def __init__(self):
        self.users = {}
        self.tokens = []
        self.posts = []

    def register_user(self, first_name, last_name, user_name, password):
        """ register() takes a first last and user name and a password.
        A new user is created and added to self.users.
        The function returns True. 
        """
        self.users[user_name] = User(first_name, last_name, user_name, password)
        return True

    def login_authentication(self, user_name, password):
        """ login_authentication() takes a user name and password as input.
        It verifies that the data is valid and returns True. If the data 
        is not correct it returns False.
        """
        try:
            if self.users[user_name].password == password:
                return True
        except Exception as message:
            print(message)

    def assign_token(self, user_name, token_string):
        """ assign_token() takes a user_name and token string as input.
        It generates a token with the Token class and adds the token to
        the self.tokens list.
        It returns the token so that it can be used in the session."""
        new_token = Token(user_name, token_string)
        self.tokens.append(new_token)
        return new_token

    def save_post(self, post):
        """ save_post() takes a post as argument and saves it to self.posts."""
        self.posts.append(post)

    def get_public_time_line(self, user_name):
        """ get_public_posts() takes a user name as input.
        It returns all the of the user in a list."""
        user_posts = []
        for post in self.posts:
            if post.user_name == user_name:
                user_posts.append(post.text)
        return user_posts

    def get_token_by_user_name(self, user_name):
        """ get_token_by_user_name() takes a user name as input and
        returns the corresponding token. This method is required for the user
        logout in the service_api."""
        for token in self.tokens:
            if user_name == token.user_name:
                return token
