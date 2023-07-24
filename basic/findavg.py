num = int(input("Enter the number: "))

def findAvg(n):
    sum = 0
    for num in range(1, n +1):
        sum = sum + num
        avg = float(sum/n)
        print('Sum = ', sum)
        return avg
print("Avg of ", num, "natural numbers = ", findAvg(num))