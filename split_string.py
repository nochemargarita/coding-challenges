import re

def split(astring, splitter):
    """Split a string by splitter and return list of splits.
        >>> split("i love balloonicorn", " ")
        ['i', 'love', 'balloonicorn']


        >>> split("that is which is that which is that", " that ")
        ['that is which is', 'which is that']

        >>> split("that is which is that which is that", "that")
        ['', ' is which is ', ' which is ', '']

        >>> split("hello world", "nope")
        ['hello world']

    """

    splitted = []
    index = 0

    while len(astring) >= index:
        current_indx = index
        # index = re.search(r'\b({})\b'.format(splitter), astring).start()
        index = astring.find(splitter, index)
        

        if index != -1:
            splitted.append(astring[current_indx:index])
            # print index
            index += len(splitter)

        else:
            splitted.append(astring[current_indx:])
            break

    return splitted

