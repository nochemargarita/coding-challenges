def firstDuplicate(a):
    """returns a duplicate whose duplicates index location is lower than the other duplicates.

    >>> firstDuplicate([2, 1, 3, 5, 3, 2])
    3

    """
    
    duplicate = -1
    index = len(a)
    for i in xrange(len(a)):
        for j in xrange(i + 1, len(a)):
            if a[i] == a[j] and j < index:
                duplicate = a[i]
                index = j
    # Its O(n^2) time and O(1) space
    # I think there will still be a better solution, O(n) time and O(1) space
    return duplicate

# a = [2, 1, 3, 5, 3, 2]

# a = [2, 4, 3, 5, 1]

# a = [2, 2]

# a = [2, 1]

# a = [2, 1, 3]

# a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]

# a = []