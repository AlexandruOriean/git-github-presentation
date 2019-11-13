import unittest
from area_of_circle import compute_area
from math import pi


class TestComputeArea(unittest.TestCase):
    def test_area(self):
        '''Checks that the area is correctly computed for positive ints'''
        self.assertAlmostEqual(compute_area(1), pi)
        self.assertAlmostEqual(compute_area(0), 0)
        self.assertAlmostEqual(compute_area(5.4), 5.4 * 5.4 * pi)

    def test_values(self):
        '''Checks that the script throws appropriate errors'''
        self.assertRaises(ValueError, compute_area, -1)

    def test_types(self):
        '''Checks that the script only takes numbers as arguments'''
        self.assertRaises(TypeError, compute_area, True)
        self.assertRaises(TypeError, compute_area, "8")
        self.assertRaises(TypeError, compute_area, 8 + 1j)
