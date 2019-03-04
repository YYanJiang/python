# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = input ("Please input the first value:")
b = input ("Please input the first value:")
c = input ("Please input the first value:")
print ("")

try:
    float(a)
    float(b)
    float(c)
    def maxOfThree(a,b,c):   
        m = max(a,b,c) 
        return m
    print("the maximum number is: ", maxOfThree(a,b,c))
    
except:
    print("please input a number!")
