def find_subset(sets):
    lst = []

    for item in sets:
        lst.append({item})

    # for indx in range(len(lst) - 1):
    #     lst.append(lst[indx] | lst[indx + 1])

    for x in sets:
        for item in range(1,len(lst)):
            lst.append(lst[x] | lst[item])



    # lst.append(lst[0] | lst[len(sets) - 1])
    # lst.append(set())

    return lst

print find_subset({1, 3, 5, 9, 5})

(1, 3)
(3, 5)
(5, 9)
(9, 5)
(1, 5)

    

