import unittest


def sum_100(nums_list):
    pass

class Test(unittest.TestCase):

    def test_sum_100_1(self):
        actual = sum_100([98, 1, 99])
        expected = [[1, 99]]

        self.assertEqual(actual, expected)

    def test_sum_100_2(self):
        actual = sum_100([95, 5, 95])
        expected = [[5, 95]]

        self.assertEqual(actual, expected)

    def test_sum_100_3(self):
        actual = sum_100([95, 5, 95, 5])
        expected = [[95, 5], [5, 95]]

        self.assertEqual(actual, expected)

    def test_sum_100_4(self):
        actual = sum_100([50, 50, 50])
        expected = [[50, 50]]

        self.assertEqual(actual, expected)

    def test_sum_100_5(self):
        actual = sum_100([50])
        expected = []

        self.assertEqual(actual, expected)

    def test_sum_100_6(self):
        actual = sum_100([50, 60, 40, 20])
        expected = [[60, 40]]

        self.assertEqual(actual, expected)

    def test_sum_100_7(self):
        actual = sum_100([5, 7, 95, 93])
        expected = [[7, 93], [5, 95]]

        self.assertEqual(actual, expected)

    def test_sum_100_8(self):
        actual = sum_100([])
        expected = []

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)