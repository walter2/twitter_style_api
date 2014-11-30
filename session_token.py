#!/user/bin/python3
# encoding: utf-8

"""
user_post.py contains the Post class for user posts.
"""

import uuid


class Token:
    """ Token is used to represent a specific logged on session from a user."""
    def __init__(self, user_name):
        self.user_name = user_name
        self.token_string = uuid.uuid4()
