#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel

from models import storage

import sys

class HBNBCommand(cmd.Cmd):
    """HBNB command interpeter"""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """exit program"""
        return True

    def do_EOF(self, args):
        """exit program"""
        return True

    def do_emptyline(self):
        pass

    def do_create(self, args):
        """create a new instance of basemodel"""
        if args is not None and args != "":
            new_args = args.split()
            if new_args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                get_ = getattr(sys.modules[__name__], new_args[0])
                newer_args = get_()
                newer_args.save()
                print(newer_args.id)
        else:
            print("** class name missing **")
            return

                
    def do_show(self, args):
        """ Prints the string representation based on the class name and id"""
        if args is not None and args != "":
            new_args = args.split()
            if new_args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(new_args) == 1:
                print ("** instance id missing **")
                return
            key = new_args[0] + "." + new_args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if len(args) < 1:
            print("** class name missing **")
        else:
            new_args = args.split()
            if len(new_args) == 1:
                if new_args[0] in self.classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                if new_args[0] in self.classes:
                    new_dict = storage.all()
                    key = f"{new_args[0]}.{new_args[1]}"
                    if key in new_dict:
                        del new_args[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
