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
        for line in sys.stdin:
            if line.rstrip() == '':
                break
            input_arguments = line.rstrip().split()
            if input_arguments[0] == '--register' or input_arguments[0] == '-r':
                if len(input_arguments) == 5:
                    service.register_user(
                            input_arguments[1],
                            input_arguments[2],
                            input_arguments[3],
                            input_arguments[4],
                            )
                else:
                    print('User registration requiers four arguments. You provided {}.' \
                           .format(len(input_arguments) - 1))
            elif input_arguments[0] == '--users' or input_arguments[0] == '-u':
                print(service.get_users())
            print('')

    except Exception as msg:
        print(msg)

if __name__ == '__main__':
    process_stdin()
