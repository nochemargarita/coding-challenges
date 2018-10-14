"""Given a pattern and a string, find if string follows the same pattern.
Here follow means a full match, such that there is a bijection between
a letter in pattern and non-empty word in string. There are long and short solutions.\

For example:

    >>> is_pattern('abba', 'dog cat cat dog')
    True

    >>> is_pattern('abba', 'dog cat cat fish')
    False
"""

def is_pattern(pattern, str):

    words = str.split()
    

        




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
