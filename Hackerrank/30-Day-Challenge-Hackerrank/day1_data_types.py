# Sample input 1:
# 12
# 4.0
# is the best place to learn and practice coding!

# Ouput:
# 16
# 8.0
# HackerRank is the best place to learn and practice coding!

# Sample input 2:
# 3
# 2.8
# is my favorite platform!

# Ouput:
# 7
# 6.8
# HackerRank is my favorite platform!

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
second_integer = int(raw_input())
double_int = float(raw_input())
s_to_concat = str(raw_input())
# Print the sum of both integer variables on a new line.
print i + second_integer
# Print the sum of the double variables on a new line.
print d + double_int

# Concatenate and print the String variables on a new line
print s + s_to_concat
# The 's' variable above should be printed first.
