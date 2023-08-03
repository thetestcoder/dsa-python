from queue import LifoQueue

def compute(num1, num2, op):
    if (op == '+'):
        return num1+num2
    elif (op == '-'):
        return num1-num2
    elif (op == '*'):
        return num1*num2
    elif (op == '/'):
        return num1/num2
    
def evaluate_postfix(input_string):
    stack = LifoQueue(maxsize=len(input_string))
    str_split = input_string.split(' ')
    print(str_split)
    for i in range(len(str_split)):
        if(str_split[i].isnumeric() == True):
            stack.put(int(str_split[i]))
        else:
            num1 = stack.get()
            num2 = stack.get()
            val = compute(num1, num2, str_split[i])
            stack.put(val)
    return stack.get()

print(evaluate_postfix('2 3 +'))