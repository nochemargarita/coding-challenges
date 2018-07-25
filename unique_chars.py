def has_unique_chars(word):
    """Returns a boolean whether the word has unique characters.

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

    """

    return len(word) == len(set(word))  # O(n) space
