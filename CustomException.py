class MyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "\nMy Exception {0}\n".format(self.message)
        else:
            return "\nInvalid input!\n"