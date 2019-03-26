# Check out the resources on the page's right side to learn more about arrays. 
# The video tutorial is by Gayle Laakmann McDowell, author of the best-selling 
# interview book Cracking the Coding Interview.

# A left rotation operation on an array shifts each of the array's elements 1
# unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], 
# then the array would become [3,4,5,1,2].

# Given an array a of n  integers and a number, d , perform d left rotations on the 
# array. Return the updated array to be printed as a single line of space-separated integers.

# Function Description

# Complete the function rotLeft in the editor below. It should return the resulting array of integers.

# rotLeft has the following parameter(s):

# An array of integers a.
# An integer d, the number of rotations.
# Input Format

# The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform. 
# The second line contains  space-separated integers .

def rotLeft(a, d):
    return a[d:] + a[:d]


print rotLeft([1,2,3,4,5], 4)  # (3,4,5,1,2)
print rotLeft([98, 67, 35, 1, 74, 79, 7, 26, 54, 63, 24, 17, 32, 81], 7) #([26, 54, 63, 24, 17, 32, 81, 98, 67, 35, 1, 74, 79, 7])