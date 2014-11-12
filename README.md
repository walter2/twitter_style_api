twitter_style_api
=================

This project implements a command line API which mimics the basic workings of twitter.

It is possible to register users and to display the registered user list.

Usage
=====

1. To start the program in the terminal type:

   $python3 start_api.py


2. To register a user you can type '--register' or '-r'. This command needs to be followed by the first, last and user name and password for the new user. If the user is registered successfully a registration message is displayed.
eg:

   --register Tim Timber timt qwerty


3. All registered users can be dispalyed with '--users' '-u'. eg:

   --u

  would display:
  
   ['timt']

4. A user can be logged in with '--login' or '-li'. The logged in user is then displayed. eg:
   -li timt qwerty


Pending features:
- session management so that only one user can be logged in
- logged in user can posts status updates
- logged in users can follow other users
- view users public time line
