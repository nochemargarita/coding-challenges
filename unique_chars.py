def has_unique_chars(word):
    """Returns a boolean whether the word has unique characters.

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

    """

    # Solution 1
    # return len(word) == len(set(word))  # O(n) space

    # Solution 2
    unique_dic = {}

    for char in word:
        if char in unique_dic:
            return False
        else:
            unique_dic[char] = 1

    return True

