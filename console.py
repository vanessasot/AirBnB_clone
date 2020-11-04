#!/usr/bin/python3
""" Create a module console """

import cmd
import shlex
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

name_of_class = {
    "BaseModel": BaseModel,
    "User": User,
}


class HBNBCommand(cmd.Cmd):
    """ Create a interpreter command in Python """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program\n """
        return True

    def emptyline(self):
        """ Nothing is executed """
        pass

    def do_create(self, args):
        """ Create a new instance of the class BaseModel """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif not args[0] in name_of_class:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """ Prints the string representation of the instance  """
        args = shlex.split(args)
        dicti = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in name_of_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) in dicti:
            print(dicti["{}.{}".format(args[0], args[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Delete a instance base on the class name and id """
        args = shlex.split(args)
        dicti = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in name_of_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) in dicti:
            dicti.pop("{}.{}".format(args[0], args[1]))
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """" Prints all strings representation of all instances """
        args = shlex.split(args)
        dicti = storage.all()
        printall = []
        if not args:
            for i in dicti.values():
                printall.append(str(v))
        elif args[0] in name_of_class:
            for key, val in dicti.items():
                if val.__class__.__name__ == args[0]:
                    printall.append(val.__str__())
            print(printall)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Update a instance base on the class name and id """
        args = shlex.split(args)
        dicti = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in name_of_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not "{}.{}".format(args[0], args[1]) in dicti:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = dicti["{}.{}".format(args[0], args[1])]
            setattr(key, args[2], args[3])
            key.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
