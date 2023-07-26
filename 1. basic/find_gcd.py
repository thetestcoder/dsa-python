#  greatest common divisor (GCD)

"""
Euclidean Algorithm:

Here's the step-by-step process:

Step 1: Take two numbers for which you want to find the GCD.
Step 2: Find the remainder of the larger number divided by the smaller number.
Step 3: Replace the larger number with the smaller number and the smaller number with the remainder obtained in Step 2.
Step 4: Repeat Steps 2 and 3 until the remainder becomes zero.
Step 5: The GCD is the last non-zero remainder obtained in Step 2.

Example:
Let's find the GCD of 48 and 18 using the Euclidean Algorithm:

Step 1: 48 and 18
Step 2: 48 ÷ 18 = 2 remainder 12
Step 3: Replace (48, 18) with (18, 12)
Step 4: 18 ÷ 12 = 1 remainder 6
Step 5: Replace (18, 12) with (12, 6)
Step 6: 12 ÷ 6 = 2 remainder 0
Step 7: Since the remainder is zero, the GCD is the last non-zero remainder, which is 6.

So, GCD(48, 18) = 6.
"""

num = input("Enter two numbers seperated by space: ")

num1 = int(num.split()[0])
num2 = int(num.split()[1])

actual_num1 = num1
actual_num2 = num2

while num2 != 0:
    t = num2
    num2 = num1%num2
    num1 = t


#print("num1 = ", num1, 'num2  = ', num2)

print(f"So, GCD({actual_num1}, {actual_num2}) = {num1}.")


