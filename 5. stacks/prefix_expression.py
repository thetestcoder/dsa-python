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
    
def evaluate_prefix(input_string):
    stack = LifoQueue(maxsize=len(input_string))
    str_split = input_string.split(' ')
    for element in str_split[:-1]:
        if(element.isnumeric() == True):
            stack.put(int(element))
        else:
            num1 = stack.get()
            num2 = stack.get()
            val = compute(num1, num2, element)
            stack.put(val)
    return stack.get()

print(evaluate_prefix('- + * 4 5 / 3 2 9'))