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


