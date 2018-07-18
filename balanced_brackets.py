def is_balanced_brackets(s):
    """returns a boolean whether a string has balanced brackets.

    >>> is_balanced_brackets('()')
    True

    >>> is_balanced_brackets('{[]}')
    True

    >>> is_balanced_brackets('{][]}')
    False

    """

    brackets = {'}': '{',
                ']': '[',
                ')': '('}
    # O(n) space
    open_brackets = set(brackets.values())
    # O(n) space
    visited = []
    # O(n) space

    for i in s: # O(n) time
        if i in open_brackets:  # O(1) time
            visited.append(i)
        elif i in brackets and brackets[i] == visited[-1]: # O(1) time
            visited.pop()
        else:
            return False

    return len(visited) == 0

# O(n) total run time
# O(n) space - need to clarify