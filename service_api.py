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
        It checks if the user name and password match
        and then logs the user in.
        """
        if self.repository.login_authentication(user_name, password):
            new_token = self.repository.assign_token(user_name)
            return new_token
        else:
            raise ValueError ('Incorrect login details. Please try again.')

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

    def get_public_time_line(self, user_name):
        """ get_public_time_line() takes a user name as input.
        It returns the public time line from this user as a list.
        """
        if user_name in self.repository.users:
            return self.repository.get_public_time_line(user_name)
        else:
            raise ValueError ('The user {0} does not exist.'.format(user_name))


    def show_following_posts(self, token):
        """ show_following_posts() takes a token as input.
        It returns a list of all users, with user names and posts, that the
        user of the token is following.
        """
        signed_in_user_following = self.repository.get_followed_users(token)
        if len(signed_in_user_following) > 0:
            following_posts = []
            for name in signed_in_user_following:
                posts = self.get_public_time_line(name)
                following_posts.append([name, posts])
                posts = []
            return following_posts
        else:
            raise ValueError ('{0} is not following any other users.'\
                               .format(token.user_name))
