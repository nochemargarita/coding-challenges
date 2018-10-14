class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str

        >>> toGoatLatin('I speak Goat Latin')
        'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'

        >>> toGoatLatin('The quick brown fox jumped over the lazy dog')
        'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
        """
        
        word_list = S.split()
        vowels = set(['a', 'e', 'i', 'o', 'u'])        
        
        for i in xrange(len(word_list)):
            if word_list[i][0].lower() in vowels:
                word_list[i] = word_list[i] + 'ma' + 'a' + ('a' * i)
            else:
                word_list[i] = word_list[i][1:] + word_list[i][0] + 'ma' + 'a' + ('a' * i)                
                
        return ' '.join(word_list)
                
testing = Solution()
print testing.toGoatLatin('I speak Goat Latin')
