"""
Program to calculate Factorial of a User entered number.
"""
factorial = 1

num = int(input("Enter Num:"))

for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)