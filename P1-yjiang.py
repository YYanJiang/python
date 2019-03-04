# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

string = input ("Please input your quiz score:\n")

try:
    score=float(string)

    if score>100 or score<0:
        print ("please input a number between 0 and 100!")
    elif score>=93:
        print("your letter grade is: A")
    elif score>=90 and score<93:
        print("your letter grade is: A-")
    elif score>=87 and score<90:
        print("your letter grade is: B+")
    elif score>=83 and score<87:
        print("your letter grade is: B")
    elif score>=80 and score<83:
        print("your letter grade is: B-")
    elif score>=70 and score<80:
        print("your letter grade is: C")
    else :
        print("your letter grade is: F")
except:
    print("please input a number!")