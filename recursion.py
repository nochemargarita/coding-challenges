def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if lst:
        return 1 + count_recursively(lst[1:])
    return 0

# print count_recursively([])
# print count_recursively([5, 6, 7])


def print_recursively(lst):
    """Print items in the list, using recursion."""

    if lst:
        print lst[0]
        return print_recursively(lst[1:])

# print_recursively([6, 2, 3])


def recursive_index(word, lst):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    index = 0
    def inner(word, lst, index):
        if index < len(lst):
            if lst[index] == word:
                return index

            index += 1
            return inner(word, lst, index)

    return inner(word, lst, index)

lst = ["hey", "there", "you"]

# print recursive_index('hey', lst)
# print recursive_index('there', lst)
# print recursive_index('you', lst)
# print recursive_index('how', [])
