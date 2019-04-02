# Task 
# Given a string, S , of length N that is indexed from 0 to N - 1, print its even-indexed 
# and odd-indexed characters as 2 space-separated strings on a single line 
# (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

number_of_input = int(raw_input())
for i in xrange(number_of_input):
    string_input = raw_input()
    print string_input[0::2], string_input[1::2]

# Input 1:
# 2
# Hacker
# Rank
# Output 1:
# Hce akr
# Rn ak

# Input 2:
# 2
# ivvkxq
# ivvkx
# Output 2:
# ivx vkq
# ivx vk