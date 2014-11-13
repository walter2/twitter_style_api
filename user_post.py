#!/user/bin/python3
# encoding: utf-8

"""
user_post.py contains the Post class for user posts.
"""


class Post:
    """ Post stores the user_name and post text for a single post."""
    def __init__(self, user_name, text):
        self.user_name = user_name
        self.text = text
