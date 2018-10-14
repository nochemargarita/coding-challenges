class Solution(object):
    def to_lower_case(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        letters = {'A': 'a',
                   'B': 'b',
                   'C': 'c',
                   'D': 'd',
                   'E': 'e',
                   'F': 'f',
                   'G': 'g',
                   'H': 'h',
                   'I': 'i',
                   'J': 'j',
                   'K': 'k',
                   'L': 'l',
                   'M': 'm',
                   'N': 'n',
                   'O': 'o',
                   'P': 'p',
                   'Q': 'q',
                   'R': 'r',
                   'S': 's',
                   'T': 't',
                   'U': 'u',
                   'V': 'v',
                   'W': 'w',
                   'X': 'x',
                   'Y': 'y',
                   'Z': 'z'}
        lower_cased = ''
        for char in str:
            if char not in letters:
                lower_cased += char
            else:
                lower_cased += letters[char]
                
        return lower_cased

solution = Solution()


def test_lower_case():
    test_cases = [
      ('Hello', 'hello'),
      ('rowInG', 'rowing'),
      ('here', 'here'),
      ('RANGE', 'range'),
      ('toss!Ng', 'toss!ng'),
      ('!@', '!@')
    ]
    for test, result in test_cases:
        my_result = solution.to_lower_case(test)
        print(test, result, my_result)
        assert my_result == result, (
            'Not there yet: ' + str(test))

test_lower_case()