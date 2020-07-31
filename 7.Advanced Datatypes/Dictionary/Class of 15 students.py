"""
Create a Dictionary for a Class of 15 students. Key would be the roll number and value would be  Attendance in the month. Ask the user to input the Roll number. Print the percentage of the Attendance for the roll number
"""

Student_Dict = {1:[82],
                2:[93],
                3:[60],
                4:[82],
                5:[92],
                6:[90],
                7:[100],
                8:[90],
                9:[96],
                10:[92],
                11:[79],
                12:[98],
                13:[80],
                14:[95],
                15:[99],}


UserInp = int(input("Enter The Roll Number Of the Student:"))


print("Student attendence is:",(Student_Dict[UserInp],[UserInp-1]))