def missing_number(nums_list, length):
    """Returns the missing number from the list."""
    # Runtime O(n)
    for i in range(1, length + 1):
        if i not in set(nums_list):
            return i


# print missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
def missing_number_2(nums_list, length):
    """Returns the missing number from the list."""
    # Runtime O(n log n)
    nums_list.sort()
    for i in range(1, length):
        if nums_list[i - 1] != i:
            return i

    return length


# print missing_number_2([2, 1, 4, 3, 6, 5, 7, 8, 9], 10)
# print missing_number_2([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
def missing_number_3(nums_list, length):
    """Returns the missing number from the list."""
    # Runtime O(n) Space O(1)

    for i in range(1, length):
        pass


# print missing_number_3([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
# print missing_number_3([2, 1, 4, 3, 6, 5, 7, 8, 9], 10)
