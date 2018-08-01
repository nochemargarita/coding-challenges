# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        self.nums = nums
        self.target = target

        for i in xrange(len(self.nums)):
            for j in xrange(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == target:
                    return [i, j]

first = Solution()
print first.twoSum([2, 7, 11, 15], 9)  # [0, 1]

second = Solution()
print second.twoSum([2, 5, 5, 11], 10)  # [1, 2]

third = Solution()
print third.twoSum([], 10)  # None

fourth = Solution()
print fourth.twoSum([1], 5)  # None

