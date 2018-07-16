def reverse_each_char(message):

    # Decode the message by reversing the words
    left = 0
    right = len(message) - 1

    while left < right:
        if message[left] != " ":
            message[left], message[right] = message[right], message[left]
        else:


        left += 1
        right -= 1

    return message

def reverse_words(reversed_chars):
    curr = 0

    for i in xrange(len(reversed_chars) + 1):
    
        if (i == len(message)) or (message[i] == ' '):
            reverse_each_char(message, current_word_index, i - 1)
            current_word_start_index = i + 1

    return reversed_characters


message = list('vault')
print reverse_words(message)
message = list('thief cake')
print reverse_words(message)
message = list('one another get')
print reverse_words(message)


