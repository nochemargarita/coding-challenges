"""Return longest word in list of words.

For example::

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

"""


def find_longest_word(words):
    """Return longest word in list of words."""

    longerst_word_length = 0

    for word in words:
        if len(word) > longerst_word_length:
            longerst_word_length = len(word)

    return longerst_word_length


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE MAX!\n")
