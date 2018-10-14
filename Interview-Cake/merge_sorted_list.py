def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    sorted_list = []  # O(n) space
    while len(my_list) > 0 or len(alices_list) > 0:  # O(n) run time
        if not my_list:
            sorted_list.append(alices_list.pop(0))
        elif not alices_list:
            sorted_list.append(my_list.pop(0))
        elif my_list[0] < alices_list[0]:
            sorted_list.append(my_list.pop(0))
        else:
            sorted_list.append(alices_list.pop(0))

    return sorted_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

my_list = []
alices_list = [1, 5, 8, 12, 14, 19]

my_list = [3, 4, 6, 10, 11, 15]
alices_list = []

my_list = [3, 4, 5, 7, 11, 30]
alices_list = [1, 5, 8, 12, 17, 19, 25, 29]  # doesn't check if num is in the merged list already, if done runtime will be o(n^2)

print merge_lists(my_list, alices_list)

# Interview cake