import unittest


class AdditionTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5, 2 + 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
