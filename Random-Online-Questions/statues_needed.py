def statues_needed(statues):
    max_height = max(statues)  # O(1) space
    min_height = min(statues)  # O(1) space
    needed_statues = 0  # O(1) space

    for i in xrange(min_height, max_height):  # O(n) runtime and O(1) space
        if i not in set(statues):  # O(n) space # O(1) runtime
            needed_statues += 1

    return needed_statues  # O(n) space # O(n) runtime


statues = [6, 2, 3, 8]
# statues = [0, 3]
# statues = []

statues_needed(statues)
