def hourglassSum(arr):
    max_sum = sum(arr[0][0:3]) + sum(arr[2][0:3]) + arr[1][1]
    for i in xrange(0,4):
        for j in xrange(0,4):
            top = arr[i][j:j+3]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j:j+3]
            curr_sum = sum(top) + sum(bottom) + mid
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum
            

test_case_1 = [
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]
              ] # 19

test_case_2 = [
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 9, 2, -4, -4, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, -1, -2, -4, 0]
              ] # 13

test_case_3 = [
                [-9, -9, -9, 1, 1, 1],
                [0, -9, 0, 4, 3, 2],
                [-9, -9, -9, 1, 2, 3],
                [0, 0, 8, 6, 6, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, 1, 2, 4, 0]
              ] # 28
