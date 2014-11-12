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
        if not first_name or not last_name or not user_name or not password:
            raise ValueError ('Please provide full user details with first, last, user name and password.')

        if user_name not in self.repository.users:
            self.repository.register_user(
                first_name,
                last_name,
                user_name,
                password
                )
            print('User \'{0}\' is registered.'.format(user_name))
            return True
        else:
            error_message = 'The user \'{0}\' exists already. Please choose another user name.'\
                             .format(user_name)
            print(error_message)
            return error_message


    def login(self, user_name, password):
        """ login() requiers a user_name and a password.
        It checks if the user name and password match and then logs the user in.
        """
        if user_name in self.repository.users: 
            if self.repository.users[user_name].password == password:
                print('{0} is now logged in'.format(user_name))
                return True
            else:
                return False
        else:
            return False


    def get_users(self):
        """ get_users() returns the currently registered self.users list."""
        users = [key for key in self.repository.users.keys()]
        return users
