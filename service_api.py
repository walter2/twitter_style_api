#!/user/bin/python3
# encoding: utf-8

"""
service_api.py implements the API through which interactions are done
with the twitter like program.
"""

import random
import string

from repository import Repository
from user_post import Post


TOKEN_LENGTH = 8


class Service:
    """ Service is the API through which the twitter like application is 
     accessed.
     At the initiation a repository is required.
    """

    def __init__(self, repository):
        self.repository = repository
        self.token_length = TOKEN_LENGTH

    def register_user(self, first_name, last_name, user_name, password):
        """register() takes the first name, last name, user name and password
        of a new user.
        It returns True if a new user is successfully registered.
        """
        if not first_name or not last_name or not user_name or not password:
            raise ValueError ('Please provide full user details with first, last, user name and password.')

        if user_name not in self.repository.users:
            self.repository.register_user(
                first_name,
                last_name,
                user_name,
                password
                )
            return True
        else:
            raise ValueError ('The user \'{0}\' exists already. Please choose another user name.'\
                             .format(user_name))

    def login(self, user_name, password):
        """ login() requiers a user_name and a password.
        It checks if the user name and password match and then logs the user in.
        """
        if self.repository.login_authentication(user_name, password):
            token_string = self.generate_token_string()
            new_token = self.repository.assign_token(user_name, token_string)
            return new_token
        else:
            raise ValueError ('Incorrect login details. Please try again.')

    def generate_token_string(self):
        """ generate_token_string() returns a random token."""
        char = string.ascii_letters
        return ''.join(random.choice(char) for character in range(self.token_length))

    def logout(self, user_name):
        """ logout() takes a user name and loggs the user out.
        If the logout was successful True is returned, otherwise False.
        """
        try:
            token = self.repository.get_token_by_user_name(user_name)
            self.repository.tokens.remove(token)
            return True
        except:
            raise ValueError ('The logout was not possible.')

    def post(self, token, text):
        """ post() takes a token and a text as input."""
        if token in self.repository.tokens:
            user_name = token.user_name
            post = Post(user_name, text)
            self.repository.save_post(post)
        else:
            raise ValueError ('The provided token is invalid and you cannot post.')

    def follow(self, token, user_name):
        """ follow() takes a token and user name as input. The process of
        following is then escalated to the repository.
        """
        self.repository.follow_users(token, user_name)
