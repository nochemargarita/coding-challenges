# given a string with parenthesis, count how many parens needed to balance.

def number_to_balance(paren_str):
    """
    >>> number_to_balance('(())')
    0

    >>> number_to_balance('(()')
    1
    
    >>> number_to_balance('(()()((')
    3

    >>> number_to_balance(')()')
    1
    """
    counter = 0

    for paren in paren_str:
        if paren == '(':
            counter += 1
        else:
            counter -= 1

    return abs(counter)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")