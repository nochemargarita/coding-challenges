def calc(s):
    """Evaluate expression.

    >>> calc("+ 1 2")  # 1 + 2
    3
    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6
    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15
    >>> calc("- 1 2")  # 1 - 2
    -1
    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3
    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
    """
    operators = {'+', '-', '/', '*'}
    
    operator_stack = []

    for i in xrange(1, len(s) + 1):
        print s[-i]


print calc("* 2 + 1 2")
        
