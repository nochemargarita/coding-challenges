def fizz_buzz():
    """print appropriate word or number.

   >>> fizz_buzz()
   1
   2
   fizz
   4
   buzz
   fizz
   7
   8
   fizz
   buzz
   11
   fizz
   13
   14
   fizzbuzz
   16
   17
   fizz
   19
   buzz
   """

    for number in xrange(1, 21):

        if (number % 3 == 0) and (number % 5 == 0):
            print 'fizzbuzz'
        elif number % 3 == 0:
            print 'fizz'
        elif number % 5 == 0:
            print 'buzz'
        else:
            print number

    # O(n) runtime and O(1) space
