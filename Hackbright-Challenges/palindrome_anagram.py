def is_palindrome(string):
    """Returns a boolean whether a str is a palindrome or not."""

    return string[::-1] == string


# print is_palindrome("racecar")
# print is_palindrome("hello")
# print is_palindrome("car")
# print is_palindrome("braces")
# print is_palindrome("mom mom")
# print is_palindrome("anna")
# print is_palindrome("")


def is_anagram(str1, str2):
    """Returns a boolean whether a string 1 is anagram or not of string 2."""

    if len(str1) != len(str2):
        return False

    result = {}  # O(n) space
    for char in str1:  # O(n) time
        if char not in result:  # O(1) time
            result[char] = 1
        else:
            result[char] += 1

    for char in str2:  # O(n) time
        if char in result:  # O(1) time
            result[char] -= 1
            if result[char] == 0:
                del result[char]

    return len(result) == 0

print is_anagram('mom', 'omm')
print is_anagram('jam', 'jom')
print is_anagram('racecar', 'arcearc')
