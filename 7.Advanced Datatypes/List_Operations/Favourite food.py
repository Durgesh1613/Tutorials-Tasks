
"""
 Create a List for favorite food Items. Store your favorite dish in that. Take input from user about their favorite dish and store it in the List from Index 1.
"""

# FOOD_ITEMS = ["Pani Puri"]

# FOODINPIT = input("ENETR THE YOUR FAVOURITE FODD ITEM:")

# FOOD_ITEMS.insert([1],FOODINPIT)

# print(FOOD_ITEMS)

""" Program to Insert element in a List """

"""Initial Blank List"""
Food = ["PaniPuri"]
print(Food)

"""Inserting 4 Elements in a List at index 0 - 3"""

for i in range(4):
    
    food = input("ENTER YOUR FAVOURITE FOOD NAME:" )

    Food.insert(i,food)

"""Print the List with Inserted Elements"""
print(Food)



