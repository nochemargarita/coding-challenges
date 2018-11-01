def ascii_deletion_distance(str1, str2):
    """
    >>> ascii_deletion_distance('at', 'cat')
    99

    >>> ascii_deletion_distance('boat', 'got')
    298

    >>> ascii_deletion_distance('thought', 'sloughs')
    674

    >>> ascii_deletion_distance('book', 'toook')
    325

    """

    result = 0
    common_characters = {}

    for character in str1:
        if character in str2:
            if character not in common_characters:
                common_characters[character] = 1
            else:
                common_characters[character] += 1
        else:
            result += ord(character)

    for character in str2:
        if character not in common_characters:
            result += ord(character)
        else:
            common_characters[character] -= 1
            if common_characters[character] >= 1:
                result = result + (ord(character) * common_characters[character])

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
