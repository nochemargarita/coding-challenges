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

    open_brackets = brackets.values()

    visited = []

    for i in s:
        if i in open_brackets:
            visited.append(i)
        elif i in brackets and i == visited[-1]:
            visited.pop()

    return len(visited) == 0
