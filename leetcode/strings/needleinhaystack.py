# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 
# if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? 
# This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().
import unittest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
  
        needle_length = len(needle)
        haystack_length = len(haystack)
        
        for indx in xrange((haystack_length - needle_length) + 1):
            if haystack[indx:indx + needle_length] == needle:
                return indx
        
        return -1
        
            
class Test(unittest.TestCase):

    def test_str_str_1(self):
        haystack = "hello"
        needle = "ll"

        actual = Solution().strStr(haystack, needle)
        expected = 2

        self.assertEqual(actual, expected)

    def test_str_str_2(self):
        haystack = "aaaaa"
        needle = "bba"

        actual = Solution().strStr(haystack, needle)
        expected = -1

        self.assertEqual(actual, expected)

    def test_str_str_3(self):
        haystack = ""
        needle = ""

        actual = Solution().strStr(haystack, needle)
        expected = 0

        self.assertEqual(actual, expected)

    def test_str_str_4(self):
        haystack = "hello"
        needle = ""

        actual = Solution().strStr(haystack, needle)
        expected = 0

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)