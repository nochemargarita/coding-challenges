"""Task:
Given an array, a, of size n distinct elements, sort the array in ascending
order using the Bubble Sort algorithm above. Once sorted, print the following 3
lines:

Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.

First Element: firstElement
where firstElement is the first element in the sorted array.

Last Element: lastElement
where lastElement is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a
running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, n, denoting the number of elements in array a.
The second line contains n space-separated integers describing the respective
values of a[0], a[1]....a[n-1].

Constraints
2 <= n <= 600
1 <= a[i] <= 2 * 10^6, where 0 <= i < n.

Output Format
Print the following three lines of output:
Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
First Element: firstElement
where firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.
"""

#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here

swap_count = 0
for i in xrange(n):
    for j in xrange(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swap_count += 1
print 'Array is sorted in {} swaps.'.format(swap_count)
print 'First Element: {}'.format(a[0])
print 'Last Element: {}'.format(a[-1])


# Sample Input 0
# 3
# 1 2 3
# Sample Output 0
# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3

# Sample Input 1
# 3
# 3 2 1
# Sample Output 1
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
