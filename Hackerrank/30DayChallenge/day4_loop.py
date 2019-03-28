# Task 
# Given an integer, n , print its first 10 multiples. Each multiple n x i 
# (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result
n = int(raw_input())
for i in xrange(1,11):
    result = n * i
    print '{} x {} = {}'.format(n, i, result)
# input 1:
# 2
# output 1:
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
# input 2:
# 7
# output 2:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
