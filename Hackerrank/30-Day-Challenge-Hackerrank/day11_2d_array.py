arr = []
for _ in xrange(6):
    print 'enter 6 digits'
    arr.append(map(int, raw_input().rstrip().split()))

max_sum = sum(arr[0][:3]) + arr[1][1] + sum(arr[2][:3])
for i in xrange(4):
    for j in xrange(4):
        top = sum(arr[i][j:j+3])
        mid = arr[i+1][j+1]
        bottom = sum(arr[i+2][j:j+3])
        total = top + mid + bottom
        if total > max_sum:
            max_sum = total

# for testting
# Sample Input 1:
# a = [1, 1, 1, 0, 0, 0]
# b = [0,1, 0, 0, 0, 0]
# c = [1, 1, 1, 0, 0, 0]
# d = [0, 0, 2, 4, 4, 0]
# e = [0, 0, 0, 2, 0, 0]
# f = [0, 0, 1, 2, 4, 0]
# Sample Output 1:
# 19

# Sample Input 2:
# a=[0, -4, -6, 0, -7, -6]
# b=[-1, -2, -6, -8, -3, -1]
# c=[-8, -4, -2, -8, -8, -6]
# d=[-3, -1, -2, -5, -7, -4]
# e=[-3, -5, -3, -6, -6, -6]
# f=[-3, -6, 0, -8, -6, -7]
# Sample Output 2:
# -19
