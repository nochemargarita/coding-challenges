import unittest

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        indx = 0
        current = 0
        while indx < len(nums):
            if nums[current] == 0:
                nums.append(nums.pop(current))
            else:
                current += 1
            
            indx += 1

        return nums


class Test(unittest.TestCase):

    def test_moveZeroes_1(self):
        actual = Solution().moveZeroes([0, 1, 0])
        expected = [1, 0, 0]

        self.assertEqual(actual, expected)

    def test_moveZeroes_2(self):
        actual = Solution().moveZeroes([0, 1, 0, 3, 12])
        expected = [1, 3, 12, 0, 0]

        self.assertEqual(actual, expected)

    def test_moveZeroes_3(self):
        actual = Solution().moveZeroes([0, 1, 0, 0, 12, 0])
        expected = [1, 12, 0, 0, 0, 0]

        self.assertEqual(actual, expected)

    def test_moveZeroes_4(self):
        actual = Solution().moveZeroes([0])
        expected = [0]

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
