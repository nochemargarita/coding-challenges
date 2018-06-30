def reverse_words(message):

    # Decode the message by reversing the words
    left = 0
    right = len(message)-1

    while left < right:
        if message[left] != " ":
            message[left], message[right] = message[right], message[left]

        left += 1
        right -= 1

    return message

message = list('vault')
# message = list('thief cake')
# message = list('one another get')

print reverse_words(message)
