#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    event create <name> <start_date> <end_date> <venue>
    event delete <event_id>
    event edit <event_id> <new_details>
    event list
    event view <event_id>
    ticket generate <email>
    ticket invalidate <ticket_id>
    event (-i | --interactive)
    event (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import datetime
import cmd
import smtplib
from docopt import docopt, DocoptExit
import functions
import db
from colorama import init
from pyfiglet import Figlet
from termcolor import *


init()
font = Figlet(font='ogre')
introd = font.renderText('Book Ticket')
os.system('cls')
cprint(introd,"green", attrs=['blink'])

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Ticket (cmd.Cmd):

    intro = 'Welcome to Ticket booking service!' \
        + ' (type help for a list of commands.)'
    print(__doc__)
    prompt = 'events>> '
    file = None

    funt = functions.Functions()


    @docopt_cmd
    def do_create(self, arg):
        """Usage: create <name> <start_date> <end_date> <venue>"""
        name = arg['<name>']
        start = datetime.datetime.strptime (arg['<start_date>'], "%Y/%m/%d") 
        end = datetime.datetime.strptime (arg['<end_date>'], "%Y/%m/%d")
        venue = arg['<venue>']

        print (self.funt.create_event(name, start, end, venue))


    @docopt_cmd
    def do_delete(self, arg):
        """Usage: delete <event_id>"""
        event = arg['<event_id>']
        delete = self.funt.delete_event(event)

    @docopt_cmd
    def do_edit(self, arg):
        """Usage: edit <event_id> <name> <start_date> <end_date> <venue> """

        try:
            id = arg['<event_id>']
            name = arg['<name>']
            start = datetime.datetime.strptime (arg['<start_date>'], "%Y/%m/%d") 
            end = datetime.datetime.strptime (arg['<end_date>'], "%Y/%m/%d")
            venue = arg['<venue>']

            print(self.funt.update_event(id, name, start, end, venue))

        except ValueError:
            print("Invalid argument")

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list"""
        print("lists of the available events")
        events = self.funt.list()

    @docopt_cmd
    def do_view(self, arg):
        """Usage: view <event_id>"""

        print(self.funt.view_event(int(arg['<event_id>'])))

    @docopt_cmd
    def do_generate(self, arg):
        """Usage: generate <email>"""
        try:
            print(self.funt.generate_ticket(arg['<email>']))
        except smtplib.SMTPException:
            print ("Error: unable to send email")


    @docopt_cmd
    def do_invalidate(self, arg):
        """Usage: invalidate <ticket_id>"""

        print(self.funt.invalidate_ticket(int(arg['<ticket_id>'])))



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thanks for booking')
        exit()

if __name__ == '__main__':
    try:
        Ticket().cmdloop()
    except KeyboardInterrupt:
        print("\nApplication stopped")
        exit()