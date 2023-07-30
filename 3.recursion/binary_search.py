def binary_search(data, target, low, high):
    if low >  high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            print(f"Value found at {mid} : {target}")
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid +1, high)
        

data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

target = int(input("Please enter the target: "))

result = binary_search(data, target, 0, len(data))

if result:
    print("Your target found in array")
else:
    print("target not found")