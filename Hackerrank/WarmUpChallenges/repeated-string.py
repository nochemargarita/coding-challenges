# Function Description

# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Input Format

# The first line contains a single string, s.
# The second line contains an integer, n.

import unittest

class Solution(object):
    def repeated_string(self, s, n):
        s_length = len(s)
        curr_count = s.count('a')

        get_quotient = n / s_length
        pre_total = get_quotient * curr_count
        get_product = get_quotient * s_length
        get_difference = n - get_product

        return pre_total + s[:get_difference].count('a')


class Test(unittest.TestCase):
    def test_repeated_string_1(self):
        actual = Solution().repeated_string('aba', 10)
        expected = 7

        self.assertEqual(actual, expected)

    def test_repeated_string_2(self):
        actual = Solution().repeated_string('a', 1000000000000)
        expected = 1000000000000

        self.assertEqual(actual, expected)


    def test_repeated_string_3(self):
        actual = Solution().repeated_string('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570)
        expected = 16481469408

        self.assertEqual(actual, expected)

    def test_repeated_string_4(self):
        actual = Solution().repeated_string('udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps', 872514961806)
        expected = 69801196944

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)