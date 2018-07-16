from itertools import combinations
def find_subset(sets):
    """return all the possible subsets.

    >>> find_subset({1, 3, 5, 9, 5})
    [(1,), (3,), (5,), (9,), (3, 1), (9, 1), (9, 3), (9, 5), (5, 1), (3, 5)]

    >>> find_subset({1, 2, 3})
    [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]

    """

    lst = []

    # for item in sets:
    #     lst.append(item)

    # for indx in range(len(lst) - 1):
    #     lst.append(lst[indx] | lst[indx + 1])

    # for x in sets:
    #     for item in range(1,len(lst)):
    #         lst.append(lst[x] | lst[item])



    # lst.append(lst[0] | lst[len(sets) - 1])
    # lst.append(set())

    # return lst

    for item in set(combinations(sets, 1)):
        lst.append(item)

    for combo in set(combinations(sets, 2)):
        lst.append(combo)

    # O(n) space
    # O(n) time
    # will have to think of an alternative way to test it since set is unoredered and possible combinations could be different.

    return lst


# print find_subset({1, 3, 5, 9, 5})
# print find_subset({1, 2, 3})

# (1, 3)
# (3, 5)
# (5, 9)
# (9, 5)
# (1, 5)

    

