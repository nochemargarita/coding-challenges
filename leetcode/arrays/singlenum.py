# Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first solution but does not pass the runtime complexity for bigger n number of items
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num

        # Second solution passed the runtime complexity but uses O(n) space/memory
        num_to_count = {}
        for num in nums:
            if num not in num_to_count:
                num_to_count[num] = 1
            else:
                num_to_count[num] += 1

        for num, count in num_to_count.iteritems():
            if count == 1:
                return num


class Test(unittest.TestCase):
    def test_single_number_1(self):
        actual = Solution().singleNumber([2, 2, 1])
        expected = 1

        self.assertEqual(actual, expected)

    def test_single_number_2(self):
        actual = Solution().singleNumber([4, 1, 2, 1, 2])
        expected = 4

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)


