"""Task
Given an array, A, of N integers, print A's elements in reverse order as a single
line of space-separated numbers.

Input Format
The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers describing array A's elements."""

n = int(raw_input())

arr = map(int, raw_input().rstrip().split())

for i in xrange(1, len(arr) + 1):
    print arr[-i],

# Sample Input 1:
# 4
# 1 4 3 2
# Sample Output 1:
# 2 3 4 1

# Sample Input 2:
# 2
# 9053 4443
# Sample Output 2:
# 4443 9053

# Sample Input 3:
# 3
# 5833 9919 6731
# Sample Output 3:
# 6731 9919 5833
