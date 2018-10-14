# def reverse(list_of_chars):
#     # Reverse the input list of chars in place
#     for i in range(len(list_of_chars)):  # O(n)
#         list_of_chars.insert(i, list_of_chars.pop())  # insert O(n), pop O(1)

#     return list_of_chars


# O(n^2)
def reverse(list_of_chars):
    # Reverse the input list of chars in place
    if list_of_chars:
        left = 0  # O(1) space
        while left < len(list_of_chars)/2 + 1:  # O(n)
            list_of_chars[left], list_of_chars[-(left + 1)] = list_of_chars[-(left + 1)], list_of_chars[left]

            left += 1

    return list_of_chars

# O(n)
# print reverse([])
# print reverse(['A', 'B', 'C', 'D', 'E'])
# print reverse(['A'])
