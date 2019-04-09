"""Task
Write a Calculator class with a single method: int power(int,int). The power
method takes two integers, n and p, as parameters and returns the integer result
of n^p. If either n or p is negative, then the method must throw an exception
with the message: n and p should be non-negative.

Note: Do not use an access modifier (e.g.: public) in the declaration for your
Calculator class.

Input Format
Input from stdin is handled for you by the locked stub code in your editor. The
first line contains an integer, T, the number of test cases. Each of the T
subsequent lines describes a test case in 2 space-separated integers denoting n
and p, respectively.

Constraints
No Test Case will result in overflow for correctly written code.
Output Format
"""

# My code
class Calculator(object):
    def power(self, n, p):
        if (n  < 0) or (p < 0):
            raise Exception('n and p should be non-negative')
        else:
            return pow(n,p)
# given
myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e

# Sample Input 1
# 4
# 3 5
# 2 4
# -1 -2
# -1 3

# Sample Output 1
# 243
# 16
# n and p should be non-negative
# n and p should be non-negative

# Sample Input 2
# 10
# 10 0
# 0 10
# -1 4
# 2 -3
# -2 -2
# 5 6
# 3 3
# 8 0
# 2 3
# 3 -3
# Sample Output 2
# 1
# 0
# n and p should be non-negative
# n and p should be non-negative
# n and p should be non-negative
# 15625
# 27
# 1
# 8
# n and p should be non-negative