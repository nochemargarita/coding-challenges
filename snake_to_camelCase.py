def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

    >>> snake_to_camel("snake_to_camel")
    'snakeToCamel'


    >>> snake_to_camel('a')
    'a'

    >>> snake_to_camel('ab')
    'ab'

    >>> snake_to_camel('a_b')
    'aB'

    >>> snake_to_camel('')
    ''

    """

    result = ''
    index = 0
    if not variable_name:
        return result
    
    while len(variable_name) >= index:
        current_indx = index
        index = variable_name.find('_', index)

        if index != -1:
            result += variable_name[current_indx:index].capitalize()

            index += len('-')

        else:
            result += variable_name[current_indx:].capitalize()
            break

    return result[0].lower() + result[1:]

    