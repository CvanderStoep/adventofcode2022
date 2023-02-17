import unittest

from day1 import compute_part_one, compute_part_two


class Day1Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(compute_part_one("test/input/day1.txt"), 24000)

    def test_part_two(self):
        self.assertEqual(compute_part_two("test/input/day1.txt"), 45000)
