"""The absolute difference between two integers, a and b, is written as |a-b|. The
maximum absolute difference between two integers in a set of positive integers,
elements, is the largest absolute difference between any two integers in elements.

The Difference class is started for you in the editor. It has a private integer
array (elements) for storing n non-negative integers, and a public integer
(maximumDifference) for storing the maximum absolute difference.

Task
Complete the Difference class by writing the following:
A class constructor that takes an array of integers as a parameter and saves it
to the elements instance variable.
A computeDifference method that finds the maximum absolute difference between
any 2 numbers in n and stores it in the maximumDifference instance variable.

Input Format
You are not responsible for reading any input from stdin. The locked Solution
class in your editor reads in  lines of input; the first line contains , and the
second line describes the  array."""


class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here

    def computeDifference(self):
        difference = max(self.__elements) - min(self.__elements)
        self.maximumDifference = difference


# Input 1:
# 3
# 1 2 5

# Output 1:
# 4

# Input 2
# 5
# 8 19 3 2 7
# Output 2:
# 17