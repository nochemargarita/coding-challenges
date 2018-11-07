# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         indices = []
#         for i, num in enumerate(nums):
#             for next_num in xrange(i + 1, len(nums)):
#                 if num + nums[next_num] == target:
#                     indices.extend([i, next_num])

#         return indices
        indices = []
        numbers_indices = {}
        for indx, num in enumerate(nums):
            if (target - num) in numbers_indices:
                indices.extend([numbers_indices[target-num], indx])
            numbers_indices[num] = indx
        return indices


class Test(unittest.TestCase):

    def test_two_sum_1(self):
        actual = Solution().twoSum([2, 7, 11, 15], 9)
        expected = [0, 1]

        self.assertEqual(actual, expected)

    def test_two_sum_2(self):
        actual = Solution().twoSum([2, 5, 5, 11], 10)
        expected = [1, 2]

        self.assertEqual(actual, expected)

    def test_two_sum_3(self):
        actual = Solution().twoSum([], 10)
        expected = []

        self.assertEqual(actual, expected)

    def test_two_sum_4(self):
        actual = Solution().twoSum([1], 5)
        expected = []

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)