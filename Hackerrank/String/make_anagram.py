"""Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's 
letters can be rearranged to form the second string. In other words, both 
strings must contain the same exact letters in the same exact frequency For 
example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption
 is dependent on the minimum number of character deletions required to make the 
 two strings anagrams. Can you help her find this number?

Given two strings, a and b, that may or may not be of the same length, determine 
the minimum number of character deletions required to make a and b anagrams. Any 
characters can be deleted from either of the strings.

For example, if a='cde' and b='dcf', we can delete e from string a and f from 
string b so that both remaining strings are cd and dc which are anagrams."""
def makeAnagram(a, b):
    char_count = {}
    similarity_count = 0

    for char in max(a,b, key=len):
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in min(b,a, key=len):
        if char in char_count:
            similarity_count += 1
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]

    return  (len(a) - similarity_count) + (len(b) - similarity_count)

# Sample Input:
# cde
# abc

# Sample Output:
# 4

# Explanation
# We delete the following characters from our two strings to turn them into 
# anagrams of each other:

# Remove d and e from cde to get c.
# Remove a and b from abc to get c.
# We must delete 4 characters to make both strings anagrams, so we print 4 on a new line.