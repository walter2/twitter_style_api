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
                     if len(input_arguments) != 3:
                         print('You entered invalid logon details. Please try again.')
                     elif not token:
                         token = service.login(input_arguments[1], input_arguments[2])
                         print('\'{0}\' is now logged in'\
                                .format(input_arguments[1]))
                     else:
                         print('Another user already logged in. Please logout first.')

                # logout users
                elif input_arguments[0] == '--logout' or input_arguments[0] == '-lo':
                    service.logout(input_arguments[1])
                    token = ''
                    print('User \'{0}\' is now logged out.'\
                           .format(input_arguments[1]))

                # post as logged in user
                elif input_arguments[0] == '--post' or input_arguments[0] == '-p':
                    new_post = ' '.join(word for word in input_arguments[1:])
                    service.post(token, new_post)
                    print('\'{0}\' posted: \'{1}\''\
                           .format(token.user_name, new_post))

                # follow other users as logged in user
                elif input_arguments[0] == '--follow' or input_arguments[0] == '-f':
                    service.follow(token, input_arguments[1])
                    print('\'{0}\' is now following: \'{1}\''\
                           .format(token.user_name, input_arguments[1]))

                # get the public time line from users
                elif input_arguments[0] == '--timeline' or input_arguments[0] == '-tl':
                    time_line = service.get_public_time_line(input_arguments[1])
                    counter = 1
                    print('Here are {0}\'s posts:'.format(input_arguments[1]))
                    for post in time_line:
                        print('{0}. {1}'.format(counter, post))
                        counter += 1

                # get posts of following users of logged in user
                elif input_arguments[0] == '--showfollowingposts' or input_arguments[0] == '-sf':
                    following_posts = service.show_following_posts(token)
                    post_counter = 1
                    print('\'{0}\' follows'.format(token.user_name))
                    for following in following_posts:
                        print('\'{0}\'s posts are:'.format(following[0]))
                        for post in following[1]:
                            print('{0}. {1}'.format(post_counter, post))
                            post_counter += 1
                        post_counter = 1
                        print('')

                # help menu
                elif input_arguments[0] == '--help' or input_arguments[0] == '-h':
                    print('''This application can be operated with:
  --help          -h   Open the help menu.
  --follow        -f   Follow add another user to the following list of the logged in user, requiered arguments: user_name
  --login         -li  Login a user, requiered arguments: user_name and password
  --logout        -lo  Log a user out, requiered arguments: user_name
  --post          -p   Post a new update for a logged in user, requiered arguments: message text
  --register      -r   Register a user, requiered arguments: first_name last_name user_name password
  --showfollowing -sf  Shows the posts of all users that the signed on user is followeding
  --timeline      -tl  Show the time line of a user, requiered arguments: user_name
''')
                # invalid input returns an error message
                else:
                    print('Invalid input. Please use \'--help\' or \'-h\' for more info.')
                print('')

            except Exception as messsage:
                print(messsage)
    except Exception as messsage:
        print(messsage)

if __name__ == '__main__':
    process_stdin()
