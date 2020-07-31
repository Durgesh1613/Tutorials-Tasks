"""Program For Number Game"""

userNum =0
calcNum = 50
UpLimit = 100
LowLimit = 0
step = 0

while userNum != "=" :
    step = step + 1


    
    calcNum = int((UpLimit+LowLimit)/2)
    userNum = input("Is your Number:" + str (calcNum) + " ")

    
    if userNum=='<':
        UpLimit = calcNum
        
    if userNum=='>':
        LowLimit = calcNum

        
print("Got the number in" + str(step) + " steps ")        