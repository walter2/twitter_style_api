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
    repository = Repository
    service = Service(repository)
    try:
        for line in sys.stdin:
            if line.rstrip() == '':
                break
            for item in line.rstrip().split():
                print('You entered:', item)
            print('')
    except Exception as msg:
        print(msg)

if __name__ == '__main__':
    process_stdin()
