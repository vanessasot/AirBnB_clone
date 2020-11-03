#!/usr/bin/python3
""" Create a module console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Create a interpreter command in Python """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def do_quit(self, args):
        """ Exit the program"""
        return True

    def help_quit(self):
        """ Help for the quit method """
        print("Quit command to exit the program")
        print()

    def emptyline(self):
        """ Nothing is executed """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
