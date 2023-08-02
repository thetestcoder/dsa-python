def count_freq(input_list):
    frequencey = {}
    for num in input_list:
        if num not in frequencey.keys():
            frequencey[num] = 1
        else:
            frequencey[num] += 1
    return frequencey

freq = count_freq([1, 2, 2, 5, 6, 5, 48, 6, 8, 7, 9, 8, 7, 5, 3, 4, 2, 1])

print(freq)