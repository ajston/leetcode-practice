# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 04:35:14 2021

@author: T14
"""

#This program is to verify if a number is an Armstrong number

#Take the input number from the user
num = int(input("Enter a number here: "))
#initialize sum
sum = 0
#find the sum of the cube of each digit
temp = num
while temp>0:
    digit = temp %10
    sum += digit**3
    temp //= 10

#display the result
if num==sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
