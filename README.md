twitter_style_api
=================

This project implements a command line API and mimics the basic workings of a platform like twitter.
It is written in Python 3.4 and is to be run in the terminal.

It is possible to register new users and to log them in and out from the terminal session. When a user is logged in he can post status updates and follow other users.
Only one user can be logged on through the terminal session.

Error messages are displayed upon invalid input.

The terminal session is ended by pressing Enter.


Usage
=====

1. To start the program in the terminal type:

   $python3 start_api.py


2. To register a user you can type '--register' or '-r'. This command needs to be followed by the first, last and user name and password for the new user. If the user is registered successfully a registration message is displayed.
eg:

   --register Tim Timber timt qwerty


3. A user can be logged in with '--login' or '-li' followed by the user name and password of the user. The logged in user is then displayed. eg:

   -li timt qwerty


4. Once a user is logged in he can post with '--post' or '-p' followed by a text. The post is then confirmed. eg:
 
   --post This is my first post.


5. A logged in user can follow other users with '--follow' or '-f' followed by a valid user name. The connection is then confirmed. eg:
 
   --follow bhill


6. A logged in user can be logged out with '--logout' or '-lo' and the user name:
 
   --logout timt


Pending features:
-----------------

- view users public time line
