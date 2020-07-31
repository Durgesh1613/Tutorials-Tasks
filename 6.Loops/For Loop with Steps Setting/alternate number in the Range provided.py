"""
Print alternate number in the Range provided by the User.
"""

R1 = int(input("Enetr The Starting Number Of Range:"))

print("Please Enter The Range You Have Decided . By add 1 in it.")

R2 = int(input("Enetr The Ending Range:"))

for i in range(R1,R2,2):
    print(i)
print("Finished printing every alternate numbers")