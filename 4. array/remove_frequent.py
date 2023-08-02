def count_freq(input_list):
    frequencey = {}
    for num in input_list:
        if num not in frequencey.keys():
            frequencey[num] = 1
        else:
            frequencey[num] += 1
    return frequencey


def remove_frequent_element(input_list):
    frequency = count_freq(input_list)
    element = -1
    max_freq = 0
    for val in frequency.keys():
        if max_freq < frequency[val]:
            max_freq = frequency[val]
            element = val
            for i in range(max_freq):
                input_list.remove(element)
    return input_list
    
updated_list = remove_frequent_element([1, 2, 2, 5, 6, 5, 48, 6, 8, 7, 9, 8, 7, 5, 3, 4, 2, 1])

print(updated_list)