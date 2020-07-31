
choice ='Y'

while(choice=='Y'):
    lenght = int(input("Enter the Lenght of Rectangle: "))
    breadth = int(input("Enter the Breadth Of Rectangle:"))
    
    Area = lenght * breadth
    
    print("Area of Rectangle is "+str(Area))
    
    choice = input("Do you to continue calculating (Enter Y/N):")

print("Thanks for using circle calculator")