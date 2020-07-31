Even_Numbers = [0,2,4,6,8]

num = int(input("Enter The number Which You Like:"))

if num > 10  :
    if (num %2) == 0:
        Even_Numbers.append(num)
        print(Even_Numbers)
    else:
        print("The Number Is Odd!Can Not Add The NUmber In the List")
else:
    print("Can Not Add The NUmber In the List")    