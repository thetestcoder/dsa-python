def hash_code(s):
    mask = (1 << 32) - 1
    h = 0
    for charactor in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(charactor)

    return h


print(hash_code("The Test Coder"))