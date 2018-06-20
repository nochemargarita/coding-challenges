def missing_number(nums_list, length):
    """Returns the missing number from the list."""
    # Runtime O(n)
    for i in range(1, length + 1):
        if i not in set(nums_list):
            return i


print missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)


def missing_number_2(nums_list, length):
    """Returns the missing number from the list."""
    # Runtime O(n log n)
    for i in range(length):
        nums_list.sort()
        nums_list[i] != i + 1


print missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)