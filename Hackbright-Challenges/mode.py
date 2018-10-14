"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    frequency = {}  # O(N) space

    for num in nums:  # O(N) time
        if num not in frequency:  # O(1) time
            frequency[num] = 1
        else:
            frequency[num] += 1

    most_frequent = max(frequency.values()) # O(N) time

    return {num for num, count in frequency.iteritems() if count == most_frequent}   # O(N) time and space


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
