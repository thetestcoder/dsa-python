num = int(input("Enter the number: "))

import math

prime = True

x = int(math.sqrt(num))

while x > 1:
    if num % x == 0:
        print(x, "divides", num)
        prime = False
        break
    else:
        x -= 1
    
if prime:
    print("The Number", num, 'is prime')
else: 
    print("The Prime", num, "isn't a prime number")