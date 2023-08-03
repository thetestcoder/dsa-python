def reverse_string(s: str):
    stack = []
    reverse_s = ''
    for i in range(len(s)):
        stack.append(s[i])
    while stack:
        reverse_s += stack.pop()
    return reverse_s

print(reverse_string("Deep"))