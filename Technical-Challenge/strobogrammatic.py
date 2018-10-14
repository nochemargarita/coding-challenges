'''
-------------------
Long-form question
-------------------
    A "Strobogrammatic Number" is a number that looks the same 
    when rotated 180 degrees (upside down) on an LED screen.
    E.g. 
       11 -> 11, Strobogrammatic
       252 -> 252, Strobogrammatic
       37 -> LE, Not!
    Write a function to determine whether a number is strobogrammatic.

    ####  ####  ####
    #        #  #
    ####  ####  ####
       #  #        #
    ####  ####  ####
'''
# 0, 1, 2, 5, 8 True
# 3, 4, 6, 7, 9 False
# First test: are all the digits in strobogrammatic_numbers?
# Second test: does each digit match it's opposite?

# FIRST SOLUTION:
# def is_strobogrammatic(number):
#     # TODO: Implement me
    
#     result = False
#     strobogrammatic_numbers = {0, 1, 2, 5, 8}
#     numbers = str(number)
#     # First test: are all the digits in strobogrammatic_numbers?
#     # Second test: does each digit match it's opposite?
     
#     for num in numbers:
#         if int(num) in strobogrammatic_numbers:
#             result = True
    
#     # print result
#     # return result
#     if (result == True) and (numbers == numbers[::-1]):
#         return True
#     else:
#         return False


def is_strobogrammatic(number):
    # TODO: Implement me

    strobogrammatic = {'0': '0',
                       '1': '1',
                       '2': '2',
                       '5': '5',
                       '8': '8',
                       '6': '9',
                       '9': '6'}  # O(1) space since I know that the number of items will be constant or will remain the same, no adding or deleting.

    to_str = str(number)  # O(1) space
    length = len(to_str)  # O(1) space

    for indx in xrange((length + 1) / 2):  # O(n) time
        last_to_mid = to_str[length-1-indx]  # O(1) space
        if last_to_mid not in strobogrammatic or \
           to_str[indx] != strobogrammatic[last_to_mid]:  # O(1) time
            return False

    return True

# O(n) time complexity
# O(1) space complexity


# '180/81' --> 3
# 1) 1 and 1 == 1 --> True
# 2) 8 and 8 == 8 -- > True
# 3) 0 and 0 == 0 --> True


def test_strobo():
    test_cases = [
      (0, True),
      (2, True),
      (3, False),
      (6, False),
      (10, False),
      (13, False),
      (11, True),
      (16, False),
      (69, True), # 96 -> tanslate -> 69
      (101, True),
      (131, False),
      (161, False),
      (18081, True),
    ]
    for test, result in test_cases:
        my_result = is_strobogrammatic(test)
        print(test, result, my_result)
        assert my_result == result, (
            'Error for value: ' + str(test))

test_strobo()