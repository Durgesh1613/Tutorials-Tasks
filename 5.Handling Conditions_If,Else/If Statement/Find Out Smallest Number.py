"""
Find out the smallest number among 2 numbers
"""
Num1 = int(input("Enter Number 1:"))

Num2 = int(input("Enter Number 2:"))

if (Num1 < Num2):
    Smallest = Num1

elif (Num2 < Num1):
    Smallest = Num2
    
print("Smallest Number is",Smallest)        