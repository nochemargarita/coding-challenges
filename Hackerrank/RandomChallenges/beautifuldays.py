"""Lily likes to play games with integers. She has created a new game where she
determines the difference between a number and its reverse. For instance, given
the number 12, its reverse is 21. Their difference is 9. The number 120 reversed
is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered
range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, [i...j] and a number k, determine the number of
days in the range that are beautiful. Beautiful numbers are defined as numbers
where | i - reverse(i) | is evenly divisible by k. If a day's value is a
beautiful number, it is a beautiful day. Print the number of beautiful days in
the range.

Function Description

Complete the beautifulDays function in the editor below.
It must return the number of beautiful days in the range.

beautifulDays has the following parameter(s):
i: the starting day number
j: the ending day number
k: the divisor"""

def beautifulDays(i, j, k):
    counter = 0
    for day in xrange(i, j + 1):
        reversed_int = int(str(day)[::-1])
        # returns a rounded whole num
        current_day = (day - reversed_int) / k
        # to check if the curr_day has a remainder or not
        has_remainder = (day - reversed_int) - (current_day * k)
        if has_remainder == 0:
            counter += 1
    return counter

# Sample Input 1:
# 20 23 6
# Sample Output 1:
# 2

# Sample Input 2:
# 949488 1753821 5005440
# Sample Output 2:
# 805

# Sample Input 2:
# 1 2000000 23047885
# Sample Output 2:
# 2998