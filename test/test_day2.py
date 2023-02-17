import unittest

from day2 import compute_part_one, compute_part_two


class Day2Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(compute_part_one("test/input/day2.txt"), 15)

    def test_part_two(self):
        self.assertEqual(compute_part_two("test/input/day2.txt"), 12)
