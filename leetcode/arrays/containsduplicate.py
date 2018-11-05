import unittest


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Longer solution
        nums.sort()
        for i in xrange(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

        # one line solution

        return len(set(nums)) != len(nums)


class Test(unittest.TestCase):

    def test_contains_duplicate_1(self):
        actual = Solution().containsDuplicate([1, 2, 3, 1])
        expected = True

        self.assertEqual(actual, expected)

    def test_contains_duplicate_2(self):
        actual = Solution().containsDuplicate([3, 1])
        expected = False

        self.assertEqual(actual, expected)

    def test_contains_duplicate_3(self):
        actual = Solution().containsDuplicate([4, 2, 1, 2, 1])
        expected = True

        self.assertEqual(actual, expected)

    def test_contains_duplicate_4(self):
        actual = Solution().containsDuplicate([0])
        expected = False

        self.assertEqual(actual, expected)

    def test_contains_duplicate_5(self):
        actual = Solution().containsDuplicate([])
        expected = False

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)