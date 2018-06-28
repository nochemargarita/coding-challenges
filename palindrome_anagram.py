def is_palindrome(string):
    """Returns a boolean whether a str is a palindrome or not."""

    boolean = False
    for i in range(len(string)/2):
        if string[i] == string[-(i + 1)]:
            boolean = True

    return boolean


# print is_palindrome("racecar")
# print is_palindrome("hello")
# print is_palindrome("car")
# print is_palindrome("braces")
# print is_palindrome("mom")
# print is_palindrome("anna")
# print is_palindrome("")


def is_anagram(str1, str2):
    """Returns a boolean whether a string 1 is anagram or not of string 2."""

    if len(str1) != len(str2):
        return False

    result = {}
    for char in str1:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    for char in str2:
        if char in result:
            result[char] -= 1
            if result[char] == 0:
                del result[char]

    return result is not None

print is_anagram('mom', 'omm')