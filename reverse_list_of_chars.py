def reverse(list_of_chars):
    # Reverse the input list of chars in place
    for i in range(len(list_of_chars)):
        list_of_chars.insert(i, list_of_chars.pop())
        
    return list_of_chars


print reverse([])
print reverse(['A', 'B', 'C', 'D', 'E'])
print reverse(['A'])
