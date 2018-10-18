# You're given strings J representing the types of stones that are jewels, and S
# representing the stones you have.  Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

import unittest


class Solution(object):
    def num_jewels_in_stones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # my_stones = {}
        # for stone in S:
        #     if stone not in my_stones:
        #         my_stones[stone] = 1
        #     else:
        #         my_stones[stone] += 1

        # return sum([my_stones.get(i, 0) for i in J])


        total = 0
        
        for i in J:
            total += S.count(i)
                
        return total


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
