"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    nums_set = set(nums)
    for num in nums:
        if -num in nums_set:
            return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n")
