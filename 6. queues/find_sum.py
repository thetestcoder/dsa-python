from queue import Queue
import math

def minpair_sum(input_list):
    que = Queue()
    for num in input_list:
        que.put(num)
    min_val = math.inf
    for i in range(len(input_list) - 1):
        num1  = que.get()
        num2 = que.get()
        que.put(num2)
        min_val = min(min_val, num1 + num2)
    return min_val

print(minpair_sum([10, 20, 30, 40, 50, 20, 10]))