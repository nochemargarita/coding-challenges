# Calculate the sum of two integers a and b, but you are not allowed 
# to use the operator + and -.

import unittest


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])

class Test(unittest.TestCase):

    def test_getSum_1(self):
        actual = Solution().getSum(-8, -12)
        expected = -20

        self.assertEqual(actual, expected)

    def test_getSum_2(self):
        actual = Solution().getSum(1, 2)
        expected = 3

        self.assertEqual(actual, expected)

    def test_getSum_3(self):
        actual = Solution().getSum(-2, 3)
        expected = 1
        
        self.assertEqual(actual, expected)

    def test_getSum_4(self):
        actual = Solution().getSum(0, -5)
        expected = -5

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)