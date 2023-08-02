def remove_duplicate(arr):
    return list(set(arr))

lst = [1, 2, 2, 23, 4, 5, 5, 6, 7, 8]

print(remove_duplicate(lst))

def remove_duplicate_2(arr):
    arr.sort()
    temp = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i+1]:
            temp.append(arr[i])
    temp.append(arr[-1])
    return temp


print(remove_duplicate_2(lst))