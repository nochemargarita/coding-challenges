def is_weird(n):
    if (n % 1 == 0) and (n % 2 != 0):
        print 'Weird'
    elif (n % 2 == 0) and (n <= 20):
        if (n >= 2) and (n <= 6):
            print 'Not Weird'
        else:
            print 'Weird'
    else:
        print 'Not Weird'


print is_weird(3)  # Weird
print is_weird(24)  # Not Weird
print is_weird(5) # Weird
print is_weird(100) # Not Weird