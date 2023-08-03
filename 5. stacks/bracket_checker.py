def bracket_chekcer(exp: str):
    stack = []
    for i in range(len(exp)):
        if exp[i] == "[":
            stack.append(exp[i])
        elif exp[i] == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True

exp = "(2+3)*4["

print(bracket_chekcer(exp))