# -*- coding: utf-8 -*-
"""
Create a blank List and insert numbers entered by the user in the List. Start insertion from Index 0
"""

# Clear_List = []

# Inp = int(input("ENTER THE NUMBER TO BE INSERTED IN THE BLANK LIST:"))


# for i in range (3):
#     Inp = int(input("ENTER THE NUMBER TO BE INSERTED IN THE BLANK LIST:"))
#     Clear_List.insert(i,Inp)
    
# print(Clear_List)    
Clear_List = []
print(Clear_List)

"""Inserting 4 Elements in a List at index 0 - 3"""

for i in range(4):
    
    number = int(input("ENTER THE NUMBER OF YOUR CHOICE:" ))

    Clear_List.insert(i,number)




"""Print the List with Inserted Element at Index 2"""
print(Clear_List)
