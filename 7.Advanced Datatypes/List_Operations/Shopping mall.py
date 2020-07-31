Items_List = ["Fruits and vegetables ",
"Beans",
"Soups",
"Nut butter", 
"Dried fruit",
"Sauces"]

done = 0
print(Items_List)

Buyed_Items=[]
while done == 0:
    items = input("Which Items You want from above options:")

    if items == "Fruits and vegetables":
        Buyed_Items.append("Fruits and vegetables")
    
    elif items == "Beans":
        Buyed_Items.append("Beans")

    elif items == "Soups":
        Buyed_Items.append("Soups")

    elif items == "Nut butter":
        Buyed_Items.append("Nut butter")

    elif items == "Dried fruit":
        Buyed_Items.append("Dried fruit")

    elif items == "Sauces":
        Buyed_Items.append("Sauces")  
    
    else:
        print("Object Is Not Avaliable")    
    More = input("Do you want more items?:")
    if More =="Yes" or More =="yes":
        done = 0
    else:
        print(Buyed_Items)
        done = 1
        print("HAVE A NICE DAY")