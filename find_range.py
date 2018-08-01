"""Given list of numbers, return smallest & largest number as a tuple.

For example::

    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

    >>> find_range([43, 3, 44, 20, 2, 1, 100, 1])
    (1, 100)



For an empty list, it should return `None` as both smallest and largest::

    >>> find_range([])
    (None, None)

Make sure it works with a list of one item, which is both smallest and
largest::

    >>> find_range([7])
    (7, 7)
"""


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""
    smallest_num = None  # O(1) space
    largest_num = None  # O(1) space

    if nums:
        if len(nums) == 1:
            smallest_num = nums[0]
            largest_num = nums[0]

        else:
            for num in nums:  # O(n) runtime
                if num < smallest_num:
                    smallest_num = num
                elif num > largest_num:
                    largest_num = num
                else:
                    smallest_num = num

    return (smallest_num, largest_num)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
