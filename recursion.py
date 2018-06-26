def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if lst:
        return 1 + count_recursively(lst[1:])
    return 0
    

print count_recursively([])
print count_recursively([5, 6, 7])