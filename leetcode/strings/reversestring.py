import unittest
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Solution 1: works but did not pass the runtime requirement
#         reversed_s = ''
        
#         for char in s:
#             reversed_s = char + reversed_s
         
#       Solution 2: Accepted.
        return s[::-1]

class Test(unittest.TestCase):

    def test_reverse_string_1(self):
        actual = Solution().reverseString('hello')
        expected = 'olleh'

        self.assertEqual(actual, expected)

    def test_reverse_string_2(self):
        actual = Solution().reverseString('A man, a plan, a canal: Panama')
        expected = 'amanaP :lanac a ,nalp a ,nam A'

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)