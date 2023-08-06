from queue import Queue
import math

def print_pairs(input_list):
    que = Queue()
    for num in input_list:
        que.put(num)
    min_val = math.inf
    for i in range(len(input_list) - 1):
        num1 = que.get()
        num2 = que.get()
        que.put(num2)
        if(abs(num1-num2) == 1):
            print(num1, num2)

print_pairs([1,2,3,4,5,2,3,6,7,8,9,2,5,4])