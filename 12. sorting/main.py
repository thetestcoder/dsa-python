def binary_search(Arr, val):
    hi, lo = len(Arr), 0
    while lo < hi:
        mid = (hi + lo) // 2
        if Arr[mid] > val:
            hi = mid -1
        elif val < Arr[mid]:
            hi = mid + 1
        else:
            return mid
    return -1

def findSumPairs(A, B, sum_val):
    A.sort()
    for i in range(0, len(B)):
        r = sum_val - B[i]
        if(binary_search(A, r) != -1):
            return 1
    return 0


A = [2, 3, 5, 7, 12, 15, 23, 32, 42]
B = [3, 13, 13, 15, 22, 33]
if(findSumPairs(A, B, 30)):
    print(True)
else:
    print(False)

