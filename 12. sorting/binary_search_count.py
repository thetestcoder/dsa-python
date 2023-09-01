def binary_search(Arr, key):
    hi, lo = len(Arr), 0
    while lo < hi:
        mid = (hi + lo) // 2
        if key == Arr[mid]:
            return key
        elif key < Arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return -1

def count_freq(Arr, k):
    index_k = binary_search(Arr, k)
    if index_k == -1:
        return -1
    count = 1
    size = len(Arr)

    for i in range(index_k+1, size):
        if Arr[i] == k:
            count += 1
        else:
            break
    for i in range(index_k -1, -1, -1):
        if Arr[i] == k:
            count += 1
        else:
            break
    return count

Arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 6, 6, 7, 8, 9]
k = 2
count = count_freq(Arr, k)
if count == -1:
    print("Number not exists")
else:
    print("Total Count of K: ", count)
