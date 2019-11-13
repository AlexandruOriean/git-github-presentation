import unittest
from area_of_circle import compute_area
from math import pi


class TestComputeArea(unittest.TestCase):
    def test_area(self):
        '''Checks that the area is correctly computed for positive ints'''
        self.assertAlmostEqual(compute_area(1), pi)
        self.assertAlmostEqual(compute_area(0), 0)
        self.assertAlmostEqual(compute_area(5.4), 5.4 * 5.4 * pi)
