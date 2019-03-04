# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

try:
    a = input ("Please enter the first value:")
    float(a)
    b = input ("Please enter the second value:")
    float(b)
    c = input ("Please enter the third value:")
    float(c)
    print ("")
        
    def maxOfThree(a,b,c):   
        m = max(a,b,c) 
        return m
    print("the maximum of ",a,",",b,",",c,"is: ", maxOfThree(a,b,c)) 
     
except:
    print("please input a number!")