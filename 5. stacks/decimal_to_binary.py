def decimal_to_binary(num: int):
    stack = []
    binary = ""
    while num:
        res = num % 2
        stack.append(res)
        num = num//2
    while stack:
        binary += str(stack.pop())
    return binary

print(decimal_to_binary(20)) 