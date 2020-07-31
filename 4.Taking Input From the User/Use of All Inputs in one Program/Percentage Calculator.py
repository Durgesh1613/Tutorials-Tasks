
"""
Print the Total marks and Percentage by taking inputs for 5 subject Marks
"""
print("PERCENTAGE CALCULATOR")
print ("EACH SUBJECT PAPER IS OF 100 MARKS")
print ("PLEASE ENTER THE MARKS ACCORDING TO THE UPPER STATEMENT")

English = int(input("ENETR THE MARKS FOR ENGLISH SUBJECT:"))
Maths = int(input("ENETR THE MARKS FOR MATHS SUBJECT:"))
Science = int(input("ENETR THE MARKS FOR sCIENCE SUBJECT:"))
Social_Studies = int(input("ENETR THE MARKS FOR SOCIAL STUDIES SUBJECT:"))
Hindi = int(input("ENETR THE MARKS FOR HINDI SUBJECT:"))

Total_Marks = English+Maths+Science+Social_Studies+Hindi
Percentage = (Total_Marks/500)*100
print ("You got",(Total_Marks),"out of 500 marks")
print("You got",Percentage,"% of 100%")