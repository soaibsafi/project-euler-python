# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:54:17 2020

@author: Soaib
"""

number = 2**1000
sum = 0
while number>0:
    sum += int(number%10)
    number //= 10
    
print(sum)



            