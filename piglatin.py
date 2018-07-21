
def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'

        >>> pig_latin('porcupines are cute')
        'orcupinespay areyay utecay'

        >>> pig_latin('give me an apple')
        'ivegay emay anyay appleyay'
    """

    words = phrase.split() # O(n) space
    vowels = set(['a', 'e', 'i', 'o', 'u']) # O(n) space

    for i in xrange(len(words)):
        if words[i][0] in vowels: # O(1) runtime
            words[i] = words[i] + 'yay'
        else:
            words[i] = words[i][1:] + words[i][0] + 'ay'

    return ' '.join(words)

    # O(n) space and runtime