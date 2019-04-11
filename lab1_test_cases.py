import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests max_list_iter in lab1.py"""

        testlist1 = []
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(testlist1)

        testlist2 = [-3]
        self.assertEqual(max_list_iter(testlist2), -3)    # check for lists with one entry

        testlist3 = [2, 5]
        self.assertEqual(max_list_iter(testlist3), 5)     # check for lists with max at last entry
        testlist4 = [5, 2]
        self.assertEqual(max_list_iter(testlist4), 5)     # check for lists with max at first entry

        testlist5 = [1, 6, 3, 5, 2]
        self.assertEqual(max_list_iter(testlist5), 6)     # check for lists with max in middle entry
        testlist6 = [-1, -3, -5, -8]
        self.assertEqual(max_list_iter(testlist6), -1)    # check for lists with negative numbers
        testlist7 = [1, 2, 5, 4, 5]
        self.assertEqual(max_list_iter(testlist7), 5)     # check for lists with duplicates max values

    def test_reverse_rec(self):
        with self.assertRaises(ValueError):                  # check for empty list
            reverse_rec([])
        self.assertEqual(reverse_rec([-1]), [-1])            # check for list with one entry
        self.assertEqual(reverse_rec([0, 5]), [5, 0])
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # check for regular list

    def test_bin_search(self):
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1

        with self.assertRaises(ValueError):                           # check for empty list
            bin_search(0, low, high, [])
        self.assertEqual(bin_search(4, low, high, list_val), 4 )      # check for entry at middle
        self.assertEqual(bin_search(2, low, high, list_val), 2 )      # check for entry between middle and low
        self.assertEqual(bin_search(8, low, high, list_val), 6)       # check for entry between middle and high
        self.assertEqual(bin_search(0, low, high, list_val), 0)       # check for entry at low
        self.assertEqual(bin_search(10, low, high, list_val),8)      # check for entry at high
        self.assertEqual(bin_search(11, low, high, list_val), None)   # check for non-existent entry greater than high
        self.assertEqual(bin_search(-1, low, high, list_val), None)   # check for non-existent entry less than low
        self.assertEqual(bin_search(6, low, high, list_val), None)    # check for non-existent entry in the middle


if __name__ == "__main__":
        unittest.main()

    
