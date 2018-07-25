def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

    >>> snake_to_camel("snake_to_camel")
    'snakeToCamel'

    """

    result = ''

    skip_index = variable_name.find('_')
    first_word = variable_name[:skip_index]
    second_word = variable_name[skip_index+1:].capitalize()

    result += first_word + second_word
    return result