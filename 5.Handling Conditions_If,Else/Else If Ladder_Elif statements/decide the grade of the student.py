"""
Enter marks in subjects, calculate percentage and based on the percentage decide the grade of the student as:

                       < 35 : Fail

                       35 - 45 : 3rd Div.

                       45 - 60: 2nd Div.

                       60 - 75: 1st Div.

                        >75 : Distinction
"""

print ("There Would Be 2 Parts In This One Code")
print(" ")
print("Following Is Part 1")
print(" ")
print("PERCENTAGE CALCULATOR")
print(" ")
print ("EACH SUBJECT PAPER IS OF 100 MARKS")
print(" ")
print ("PLEASE ENTER THE MARKS ACCORDING TO THE UPPER STATEMENT")
print(" ")
English = int(input("ENETR THE MARKS FOR ENGLISH SUBJECT:"))
Maths = int(input("ENETR THE MARKS FOR MATHS SUBJECT:"))
Science = int(input("ENETR THE MARKS FOR sCIENCE SUBJECT:"))
Social_Studies = int(input("ENETR THE MARKS FOR SOCIAL STUDIES SUBJECT:"))
Hindi = int(input("ENETR THE MARKS FOR HINDI SUBJECT:"))
Total_Marks = English+Maths+Science+Social_Studies+Hindi
Percentage = (Total_Marks/500)*100
print(" ")
print ("You got",(Total_Marks),"out of 500 marks")
print(" ")
print("You got",Percentage,"% of 100%")
print(" ")
print ("Following Is Part 2")
print(" ")
print("Deciding Grades")
if Percentage < 35 :
    print("Fail")
elif Percentage >=35 and Percentage <45:
    print("3rd Division") 
elif Percentage >=45 and Percentage <60:
    print("2nd Division")
elif Percentage >=60 and Percentage <75:
    print("1st Division")    
elif Percentage >=75:
    print("Distinction")    
    