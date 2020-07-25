import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_sort_int(self):
        self.assertEqual(sort_list([20, 1, 43, 2]), [43, 20, 2, 1])
        self.assertEqual(sort_list([4, 3, 5, 4]), [5, 4, 4, 3])
        self.assertEqual(sort_list([432, 4, 6, 43]), [432, 43, 6, 4])

    def test_list_string(self):
        self.assertEqual(list_string([43, 20, 2, 1]), '432021')
        self.assertEqual(list_string([5, 4, 4, 3]), '5443')
        self.assertEqual(list_string([432, 43, 6, 4]), '4324364')

    def test_string_int(self):
        self.assertEqual(string_int('432021'), 432021)
        self.assertEqual(string_int('5443'), 5443)
        self.assertEqual(string_int('4324364'), 4324364)
