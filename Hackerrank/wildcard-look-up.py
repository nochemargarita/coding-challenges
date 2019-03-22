# Note: Can't use regex
import unittest


class Solution(object):
    def is_member(self, query, words):
        for word in words:
            if len(word) == len(query):
                for i in xrange(len(word)):
                    if query[i] != word[i] and query[i] != '*':
                        break
                else:
                    return True
        return False


class Test(unittest.TestCase):

    def test_contains_duplicate_1(self):
        actual = Solution().is_member('bar', ['foo', 'bar', 'fizz'])
        expected = True

        self.assertEqual(actual, expected)

    def test_contains_duplicate_2(self):
        actual = Solution().is_member('d*g', ['dig', 'bag', 'fuzz'])
        expected = True

        self.assertEqual(actual, expected)

    def test_contains_duplicate_3(self):
        actual = Solution().is_member('****', ['dig', 'bag', 'fuzz'])
        expected = True

        self.assertEqual(actual, expected)

    def test_contains_duplicate_4(self):
        actual = Solution().is_member('d**g', ['dig', 'bag', 'fuzz'])
        expected = False

        self.assertEqual(actual, expected)
    
    def test_contains_duplicate_5(self):
        actual = Solution().is_member('fu*z*', ['dig', 'bag', 'fuzz'])
        expected = False

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)