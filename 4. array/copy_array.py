def copy_array(input_arr):
    copied_array = [None] * len(input_arr)
    for i in range(len(input_arr)):
        copied_array[i] = input_arr[i]
    return copied_array

new_arr = copy_array([1, 2, 3, 4, 5, 6, 7, 8])

print(new_arr)