#!/user/bin/python3
# encoding: utf-8

"""
start_api.py runs from the command line.
Once started it takes command line arguments which are then passed to the 
service module.
"""

import sys

from repository import Repository
from service_api import Service


def process_stdin():
    """ process_stdin() is a infinite loop which takes the stdin line by line
    and processes the given commands on the service accordingly.
    The function terminates by pressing Enter.
    """
    #initiation of repository and service
    repository = Repository()
    service = Service(repository)
    try:
        token = ''
        for line in sys.stdin:
            try:
                if line.rstrip() == '':
                    break
                input_arguments = line.rstrip().split()
                # register users
                if input_arguments[0] == '--register' or input_arguments[0] == '-r':
                    if len(input_arguments) == 5:
                        service.register_user(
                                input_arguments[1],
                                input_arguments[2],
                                input_arguments[3],
                                input_arguments[4],
                                )
                        print('User \'{0}\' is registered.'\
                               .format(input_arguments[3]))
                    else:
                        print('User registration requiers four arguments. You provided {}.' \
                               .format(len(input_arguments) - 1))
                # login users
                elif input_arguments[0] == '--login' or input_arguments[0] == '-li':
                     if not token:
                         token = service.login(input_arguments[1], input_arguments[2])
                         print('{0} is now logged in'.format(input_arguments[1]))
                     else:
                         print('Another user already logged in. Please logout first.')
                # logout users
                elif input_arguments[0] == '--logout' or input_arguments[0] == '-lo':
                    service.logout(input_arguments[1])
                    token = ''
                    print('User {0} is now logged out.'.format(input_arguments[1]))
                # logged in users can post
                elif input_arguments[0] == '--post' or input_arguments[0] == '-p':
                    new_post = ' '.join(word for word in input_arguments[1:])
                    service.post(token, new_post)
                    print('{0} posted: \'{1}\''.format(token.user_name, new_post))
                # invalid input returns an error message
                else:
                    print('Invalid input. Please try again.')
                print('')

            except Exception as messsage:
                print(messsage)
    except Exception as messsage:
        print(messsage)

if __name__ == '__main__':
    process_stdin()
