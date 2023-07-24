num = int(input("Please enter a number: "))

fact = 1

for x in range(2, num+1):
    fact = fact * x

print(fact)