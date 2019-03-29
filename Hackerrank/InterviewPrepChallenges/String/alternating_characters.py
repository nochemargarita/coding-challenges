"""You are given a string containing characters A and B only. Your task is to
change it into a string such that there are no matching adjacent characters.
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s=AABAAB, remove an A at positions 0 and 3 to make
s=ABAB in 2 deletions.

Function Description

Complete the alternatingCharacters function in the editor below. It must return
an integer representing the minimum number of deletions to make the alternating
string.

alternatingCharacters has the following parameter(s):

s: a string
Input Format

The first line contains an integer q, the number of queries.
The next q lines each contain a string s."""

def alternatingCharacters(s):
    counter = 0
    curr_char = s[0]
    for i in xrange(1, len(s)):
        if s[i] == curr_char:
            counter += 1
        curr_char = s[i]

    return counter

# Sample Input 1:
# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB
# Sample Output 2:
# 3
# 4
# 0
# 0
# 4

# Sample Input 2:
# 10
# ABABBABAAB
# BABAABBAAB
# AAAABBAAAA
# BABBABABBA
# AABBBBAAAA
# BAAAABBBBB
# BBABAAAABB
# BBBAAABBAB
# BABAAABBBB
# AAAABAABBB

# Sample Output 2:
# 2
# 3
# 7
# 2
# 7
# 7
# 5
# 5
# 5
# 6
