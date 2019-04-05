from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display():
        pass
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    def display(self):
        print 'Title: {}'.format(self.title)
        print 'Author: {}'.format(self.author)
        print 'Price: {}'.format(self.price)

# Input 1:
# The Alchemist
# Paulo Coelho
# 248

# Expected Output 1:
# Title: The Alchemist
# Author: Paulo Coelho
# Price: 248

# Input 2:
# Five Point Someone
# Chetan Bhagat
# 270

# Expected Output 2:
# Title: Five Point Someone
# Author: Chetan Bhagat
# Price: 270