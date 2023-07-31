def product(num1, num2, val):
    if num2 == 0:
        return val
    else:
        num2 -= 1
        val += num1
        return product(num1, num2, val)
    

num1 = 12
num2  = 5

print(product(num1, num2, 0))