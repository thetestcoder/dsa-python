import math

def recursive_list(input_list, index, curr_max, curr_min):
    if index == len(input_list):
        return (curr_min, curr_max)
    else:
        curr_max = max(curr_max, input_list[index])
        curr_min = min(curr_min, input_list[index])
        return recursive_list(input_list, index+1, curr_max, curr_min)
    

data = [1,2,3,4,5,9,25,56,44,55,66,77,8,99,2000,33,6669,999900,99990]

min_max_tuple = recursive_list(data, 0, -math.inf, math.inf)
print(min_max_tuple)