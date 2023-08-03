from queue import LifoQueue

class CustomLifo(LifoQueue):
    def top(self):
        num = self.get()
        self.put(num)
        return num

def infix_postfix(input_string):
    input_string.replace(" ", "")
    stack = CustomLifo(len(input_string))
    precedence = {'+':1, '-':1, '*':2, '/':2, '^': 3}
    postfix = ""
    for char in input_string:
        if (char == ')'):
            while(stack.top != '('):
                postfix += stack.get()
            stack.get()
            continue
        elif (char == '('):
            stack.put(char)
            continue
        elif (ord(char) >= ord('a') and ord(char) <= ord('z')):
            postfix += char
            continue
        elif (stack.empty() == True or stack.top() == '(' or precedence[char] > precedence[stack.top()]):
            stack.put(char)
        elif(precedence[char] <= precedence[stack.top()]):
            while(stack.empty() == False and stack.top() != '(' and precedence[stack.top()] >= precedence[char]):
                postfix += stack.get()
            stack.put(char)
    while(stack.empty() == False):
        postfix += stack.get()
        return postfix

def infix_prefix(input_string):
    input_string = input_string[:-1]
    prefix_reverse = infix_prefix(input_string)
    prefix = prefix_reverse[:-1]
    return prefix
