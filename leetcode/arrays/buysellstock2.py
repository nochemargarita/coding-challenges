import unittest


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_prof = 0
        for i in xrange(len(prices) - 1):
            buy = prices[i]
            sell = prices[i + 1]
            if sell - buy > 0:
                max_prof = max_prof +  (sell - buy)
        
        return max_prof


class Test(unittest.TestCase):

    def test_max_profit_1(self):
        actual = Solution().maxProfit([7,1,5,3,6,4])
        expected = 7

        self.assertEqual(actual, expected)

    def test_max_profit_2(self):
        actual = Solution().maxProfit([1,2,3,4,5])
        expected = 4

        self.assertEqual(actual, expected)

    def test_max_profit_3(self):
        actual = Solution().maxProfit([7,6,4,3,1])
        expected = 0

        self.assertEqual(actual, expected)

    def test_max_profit_4(self):
        actual = Solution().maxProfit([9, 1])
        expected = 0

        self.assertEqual(actual, expected)

    def test_max_profit_5(self):
        actual = Solution().maxProfit([])
        expected = 0

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)