# Function Description

# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

# sockMerchant has the following parameter(s):

# ar: the colors of each sock

import unittest

class Solution(object):
    def sock_merchant(self, ar):
        sock_to_count = {}

        for item in ar:
            if item not in sock_to_count:
                sock_to_count[item] = 1
            else:
                sock_to_count[item] += 1

        return sum([count/2 for sock, count in sock_to_count.iteritems() if count >= 2])


class Test(unittest.TestCase):
    def test_sock_merchant_1(self):
        actual = Solution().sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
        expected = 3

        self.assertEqual(actual, expected)

    def test_sock_merchant_2(self):
        actual = Solution().sock_merchant([10, 30, 20, 40, 10, 70, 50, 10, 20])
        expected = 2

        self.assertEqual(actual, expected)


    def test_sock_merchant_3(self):
        actual = Solution().sock_merchant([4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5])
        expected = 9

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)