from collections import deque

def check_paliamdrome(input_str):
    str_dequeue = deque(input_str)
    for i in range(len(input_str)//2):
        if(input_str[i] != input_str[-1-i]):
            return False
    return True

print(check_paliamdrome('racecar'))