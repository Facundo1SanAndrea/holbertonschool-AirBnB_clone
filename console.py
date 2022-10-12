#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""



import cmd


class HBNBCommand(cmd.Cmd):
    """command interpeter"""

    prompt: '(hbnb) '

    def do_quit(self, args):
        """exit program"""
        return True

    def do_EOF(self, args):
        """exit program"""
        return True

    def do_empty_line(self):
        """skip next line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
