"""Task
Read a string, S, and print its integer value; if S cannot be converted to an
integer, print Bad String.

Note:
You must use the String-to-Integer and exception handling constructs built into
your submission language. If you attempt to use loops/conditional statements,
you will get a 0 score.

Input Format

A single string, S."""


S = raw_input().strip()

try:
    print int(S)
except:
    print 'Bad String'


# Sample Input 0
# 3
# Sample Output 0
# 3

# Sample Input 1
# za
# Sample Output 1
# Bad String