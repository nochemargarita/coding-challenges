import unittest

def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0

    for char in word:
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count > (len(word) - vowel_count)



class Test(unittest.TestCase):

    def test_more_vowels_1(self):
        actual = has_more_vowels('moose')
        expected = True

        self.assertEqual(actual, expected)

    def test_more_vowels_2(self):
        actual = has_more_vowels('mice')
        expected = False

        self.assertEqual(actual, expected)

    def test_more_vowels_3(self):
        actual = has_more_vowels('graph')
        expected = False

        self.assertEqual(actual, expected)

    def test_more_vowels_4(self):
        actual = has_more_vowels('yay')
        expected = False

        self.assertEqual(actual, expected)

    def test_more_vowels_5(self):
        actual = has_more_vowels('Aal')
        expected = True

        self.assertEqual(actual, expected)

    def test_more_vowels_6(self):
        actual = has_more_vowels('')
        expected = False

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)