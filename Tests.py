import unittest
from Controller import *


class Tests(unittest.TestCase):

    def test_input_int(self):
        with self.assertRaises(ValueError):
            input_int()
        

    # def test_input_eq(self):
    #     base = input_Eq()
    #     self.assertEqual(base, Equipment("", 0, "", "", 0, 1, 1))
    
    def test_loading(self):
        with self.assertRaises(IOError):
            load("safe.dat")


if __name__ == '__main__':
        unittest.main()