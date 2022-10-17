#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""
import cmd
import sys
import uuid
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine import file_storage
from models import storage



class HBNBCommand(cmd.Cmd):
    """HBNB command interpeter"""

    prompt = "(hbnb)"

    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "Place": Place, "State": State, "Review": Review}
 
    def do_quit(self, args):
        """exit program"""
        return True

    def do_EOF(self, args):
        """exit program"""
        return True

    def emptyline(self):
        """skip next line"""
        pass

    def do_create(self, args):
        """create a new instance of basemodel"""
        #class no args
        if len(args)  < 1:
            print("** class name missing **")
            return
        #class with args
        if args == 'BaseModel':
            _object = models.base_model.BaseModel()
        else:
            print("** class doesn\'t exist **")
            return
        models.storage.save()
        print(_object.id)

                
    def do_show(self, args):
        """ Prints the string representation based on the class name and id"""
        if args is not None and args != "":
            new_args = args.split()
            #has no first args
            if new_args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            #Has first args , checks wat is
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
        #Checks for the len an args
        if len(args) < 1:
            print("** class name missing **")
        else:
            new_args = args.split()
            #checks is it has a rgs , and if it is one the clases
            if len(new_args) == 1:
                if new_args[0] in self.classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                #if args is in classes
                if new_args[0] in self.classes:
                    new_dict = storage.all()
                    key = f"{new_args[0]}.{new_args[1]}"
                    if key in new_dict:
                        new_dict.pop(key)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all 
        instances based or not on the class name"""
        new_dict = storage.all()
        new_list = []
        if len(args) < 1:
            for key in new_dict:
                _obj = new_dict[key]
                new_list.append(str(_obj))
            print(new_list)
        else:
            list_ = args.split()
            if list_[0] in self.classes:
                for key, value in new_dict.items():
                    if list_[0] == value.__class__.__name__:
                        _obj = new_dict[key]
                        new_list.append(str(_obj))
                print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """update instance of class name and id"""
        _list = args.split()
        if len(_list) == 0:
            print("** class name missing **")
            return
        if _list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(_list) == 1:
            print("** instance id missing **")
            return
        key = _list[0] + "." + _list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(_list) == 2:
            print("** attribute name missing **")
            return
        if len(_list) == 3:
            print("** value missing **")
            return
        storage.all()[key].__dict__[_list[2]] = _list[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
