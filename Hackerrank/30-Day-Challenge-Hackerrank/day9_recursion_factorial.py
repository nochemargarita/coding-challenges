"""Task
Write a factorial function that takes a positive integer, N as a parameter and
prints the result of N!(N factorial).

Note: If you fail to use recursion or fail to name your recursive function
factorial or Factorial, you will get a score of 0.

Input Format
A single integer, N(the argument to pass to factorial)."""


def factorial(n):
    if n != 1:
        return n*factorial(n-1)
    return n

# Sample Input 1:
# 3

# Sample Output 1:
# 6

# Sample Input 2:
# 5
# Sample Output 2:
# 120
