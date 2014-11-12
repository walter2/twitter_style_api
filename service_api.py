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
     At the initiation a repository is requried.
    """

    def __init__(self, repository):
        self.repository = repository
