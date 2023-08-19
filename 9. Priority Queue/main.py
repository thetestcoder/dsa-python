from heapq import *

def greater_equal(li, value, index):
    if(li[index] > value):
        return 0
    else:
        left = 0
        right = 0
        if (2 * index + 1 < len(li)):
            left = greater_equal(li, value, 2* index+1)
        if( 2 * index + 2 < len(li)):
            right = greater_equal(li, value, 2 * index + 2)
        return 1 + left + right

li = [5, 7, 9, 1, 3] 
heapify(li)
value = 10
index = 0

print(greater_equal(li, value, index))