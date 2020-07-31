
"""
Print the table of number entered by the user
"""

num = int(input("Enter the Number Of Table You Want to know:"))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)