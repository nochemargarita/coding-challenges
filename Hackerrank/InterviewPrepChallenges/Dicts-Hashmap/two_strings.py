""""Given two strings, determine if they share a common substring. A substring may
be as small as one character.

For example, the words "a", "and", "art" share the common substring a. The words
"be" and "cat" do not share a substring.

Function Description:
Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

twoStrings has the following parameter(s):

s1, s2: two strings to analyze .
Input Format

The first line contains a single integer p, the number of test cases.

The following p pairs of lines are as follows:

The first line contains string s1.
The second line contains string s2."""
def twoStrings(s1, s2):
    # Solution 1:
    # to_compare = set(max(s1,s2, key=len) )
    # return char in min(s2, s1, key=len):
    #     if char in to_compare:
    #         return 'YES'
    
    # return 'NO'
    # Solution 2:
    return 'YES' if any(char in set(s1) for char in set(s2)) else 'NO'


# Sample Input 1:
# 2
# hello
# world
# hi
# world

# Sample Output 1:
# YES
# NO

# Sample Input 2:
# 4
# wouldyoulikefries
# abcabcabcabcabcabc
# hackerrankcommunity
# cdecdecdecde
# jackandjill
# wentupthehill
# writetoyourparents
# fghmqzldbc

# Sample Output 2:
# NO
# YES
# YES
# NO