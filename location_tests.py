import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):                          # added additional test for __eq__
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.3, 0)
        self.assertEqual(loc1, loc2)
        assert(loc1 != loc3)

if __name__ == "__main__":
        unittest.main()
