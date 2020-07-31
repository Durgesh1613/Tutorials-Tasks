# -*- coding: utf-8 -*-
"""
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
"""

print(" ")
print("                                  SQUARES                                      ")
print(" ")
print("IN THIS PROGRAM WE WOULD FIND OUT THE SQUARES")
print(" ")
#
#n=int(input("Enter a number:"))
#d={x:x*x for x in range(1,n+1)}
#print(d)

# Python Program to Create Dictionary of keys and values are square of keys

number = int(input("Please enter the Maximum Number : "))
myDict = {}

for x in range(1, number + 1):
    myDict[x] = x ** 2
    
print("SQUAES TILL THE NUMBER YOU ENTERED", myDict)