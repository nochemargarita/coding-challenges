# Given two strings s and t , write a function to determine if t is an anagram of s.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

import unittest


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1: better run time
        if len(s) != len(t):
            return False
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        
        return True

        # Longer Solution using dictionary
#         letter_count = {}
#         for char in s:
#             if char not in letter_count:
#                 letter_count[char] = 1
#             else:
#                 letter_count[char] += 1
        
#         for char in t:
#             if char not in letter_count:
#                 return False
#             else:
#                 letter_count[char] -= 1
#                 if letter_count[char] == 0:
#                     del letter_count[char]
#         return letter_count == {}
                
        # Solution 3: sort both items and see if equal or not.
        # return sorted(t) == sorted(s)


class Test(unittest.TestCase):

    def test_is_anagram_1(self):
        actual = Solution().isAnagram('anagram', 'nagaram')
        expected = True

        self.assertEqual(actual, expected)

    def test_is_anagram_2(self):
        actual = Solution().isAnagram('rat', 'car')
        expected = False

        self.assertEqual(actual, expected)

    def test_is_anagram_3(self):
        actual = Solution().isAnagram('ab', 'a')
        expected = False

        self.assertEqual(actual, expected)

    def test_is_anagram_4(self):
        actual = Solution().isAnagram('', '')
        expected = True

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)