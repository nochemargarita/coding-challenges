import unittest


def has_balanced_brackets(string):
    """returns a boolean whether a string has balanced brackets."""

    brackets = {'}': '{',
                ']': '[',
                ')': '(',
                '>': '<'}  # O(1) space
    # open_brackets = set(brackets.values())  # O(1) space # O(n) time
    seen_open_brackets = []  # O(n) space

    # for char in string:
    #     if char in open_brackets:
    #         seen_open_brackets.append(char)

    #     elif char in brackets:
    #         if seen_open_brackets == []:
    #             return False
    #         elif brackets[char] == seen_open_brackets[-1]:
    #             seen_open_brackets.pop()
    #         else:
    #             return False

    # return seen_open_brackets == []

    # O(n) total run time
    # O(n) total space complexity

    # Solution 2: Improved overall runtime
    for i in string:
        if i not in brackets:
            seen_open_brackets.append(i)
        elif seen_open_brackets != [] and brackets[i] == seen_open_brackets[-1]:
            seen_open_brackets.pop()
        else:
            return False
    if seen_open_brackets == []:
        return True
    else:
        return False  



class Test(unittest.TestCase):

    def test_balanced_brackets_1(self):
        actual = has_balanced_brackets('<>')
        expected = True

        self.assertEqual(actual, expected)

    def test_balanced_brackets_2(self):
        actual = has_balanced_brackets('<[]>')
        expected = True

        self.assertEqual(actual, expected)

    def test_balanced_brackets_3(self):
        actual = has_balanced_brackets('<[{()}]>')
        expected = True

        self.assertEqual(actual, expected)

    def test_balanced_brackets_4(self):
        actual = has_balanced_brackets('<>[{()}]>')
        expected = False

        self.assertEqual(actual, expected)

    def test_balanced_brackets_5(self):
        actual = has_balanced_brackets('<[{(<}]>')
        expected = False

        self.assertEqual(actual, expected)


    def test_balanced_brackets_6(self):
        actual = has_balanced_brackets('>()')
        expected = False

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)