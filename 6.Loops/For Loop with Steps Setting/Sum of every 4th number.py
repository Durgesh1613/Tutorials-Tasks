"""
Calculate the Sum of every 4th number in the Range given by the User.
"""

R1 = int(input("Enetr The Starting Number Of Range:"))

print("Please Enter The Range You Have Decided . By add 1 in it.")

R2 = int(input("Enetr The Ending Range:"))

for i in range(R1,R2,1):
    print(i)
    
print("Printing 4th Number")    
for j in range(R1,R2,4):
    S4 = j+j
    print(j)    
print("Sum Of Every 4th Nmber Is"+str(S4))