
# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
            
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9

# Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.

# Sample output (pseudocode):
# [
#   [1, 2, 4],   // Individuals with zero parents
#   [5, 7, 8, 9] // Individuals with exactly one parent
# ]



# iterate over each item
# check if item[0] exists in other items[1]
# if it does not exits, add to zeroParents = []
# dictionary key(item[1]):value(counter)


def with_and_without_parents(pairs):
    """returns a list that containing a list of item w/o parents and another list with 1 parent."""

    without_parent = []
    with_one_parent = []
    counter_dictionary = {}

    for i in xrange(len(pairs)):
        if pairs[i][1] not in counter_dictionary:
            counter_dictionary[pairs[i][1]] = 1
        else:
            counter_dictionary[pairs[i][1]] += 1

        
    for item, count in counter_dictionary.iteritems():
        if count == 1:
          with_one_parent.append(item)

    return with_one_parent



parent_child_pairs = [
                      [1, 3], [2, 3], [3, 6], [5, 6],
                      [5, 7], [4, 5], [4, 8], [8, 9]
                     ]


print with_and_without_parents(parent_child_pairs)                    