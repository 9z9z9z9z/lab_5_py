import unittest
from Controller import *


class Tests(unittest.TestCase):

    def test_input_int_type(self):
        with self.assertRaises(ValueError):
            input_int("Need a ValueError")

    def test_input_int_custom(self):
        with self.assertRaises(MyException):
            input_int("Need a MyException")
    
    def test_loading(self):
        with self.assertRaises(IOError):
            load(input("Input name of file:\t"))


if __name__ == '__main__':
        unittest.main()