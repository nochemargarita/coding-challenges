class Person:
    age = None
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if self.initialAge < 0:
            self.age = 0
            print 'Age is not valid, setting age to 0.'
        else:
            self.age = self.initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print 'You are young.'
        elif self.age >= 13 and self.age < 18:
            print 'You are a teenager.'
        else:
            print 'You are old.'
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
# Input 1:
# sample_1 = Person(-1) # Age is not valid, setting age to 0.
# sample_1.amIOld() # You are young.
# sample_1.yearPasses()
# sample_1.amIOld() # You are young.
# Input 2:
# sample_2 = Person(10)
# sample_2.amIOld() # You are young.
# sample_2.yearPasses()
# sample_2.amIOld() # You are young.
# Input 3:
# sample_3 = Person(17)
# sample_3.amIOld() # You are a teenager.
# sample_3.yearPasses()
# sample_3.amIOld() # You are old.
# Input 4:
# sample_4 = Person(18)
# sample_4.amIOld() # You are old.
# sample_4.yearPasses()
# sample_4.amIOld() # You are old.
