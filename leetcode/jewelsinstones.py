import unittest


class Solution(object):
    def num_jewels_in_stones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        my_stones = {}
        for stone in S:
            if stone not in my_stones:
                my_stones[stone] = 1
            else:
                my_stones[stone] += 1

        return sum([my_stones.get(i, 0) for i in J])


class Test(unittest.TestCase):

    def test_num_jewels_in_stones_1(self):
        J = "aA"
        S = "aAAbbbb"
        actual = Solution().num_jewels_in_stones(J, S)
        expected = 3

        self.assertEqual(actual, expected)

    def test_num_jewels_in_stones_2(self):
        J = "z"
        S = "ZZ"
        actual = Solution().num_jewels_in_stones(J, S)
        expected = 0

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
