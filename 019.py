# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:04:00 2020

@author: Soaib
"""

""""
Solution 1:
Using python 'datetime' package.
It is the most trivial solution. 
We can loop through the all years and count if the weekday() is sunday(0)
"""
from datetime import date
sundays = 0
for i in range(1901, 2001, 1):
    for j in range(1, 13, 1):
        if date(i,j,1).weekday() == 6:
            sundays += 1
print(sundays)
    


""""
Solution 2:
Without using python's default package we can make solve it by ourself using  Zeller's congruence.
This is the algorithm to calculate the day of the week of Gregorian Calendar-
h = q + floor((13*(month[m]+1)/5)) + K + floor(K/4) + floor(J/4) + 5*J) % 7
​
where,
    h = day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
    q is the day of the month
    m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February)
    K the year of the century (year \bmod 100yearmod100).
    J is the zero-based century (actually year / 100) For example, the zero-based centuries for 1995 and 2000 are 19 and 20 respectively 
"""     
import math
def day_of_the_week(y, m, q):
    J = y//100
    K = y%100
    month = [13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    return (q + math.floor((13*(month[m]+1)/5)) + K + math.floor(K/4) + math.floor(J/4) - 2*J) % 7

""""
Now we can we can solve the problem by ourself according to previous solution.
"""
def total_sundays():
    sundays = 0
    for i in range(1901, 2001, 1):
        for j in range(12):
            if day_of_the_week(i,j,1)== 0:
                sundays += 1             
    return sundays

print(total_sundays())





""""
Solution 3:
The above describes solution is more general purpose.
For this Specific problem we can solve it by using hermonic rule.
"""
def count_sundays():
    sundays, weekday = 0, 2
    months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    
    for i in range(1901, 2001, 1):
        months[1] = 28 + (i % 4 == 0 and i % 100 != 0 or i % 400 == 0)
        for month in months:
            weekday += month % 7
            if weekday % 7 == 0:
                sundays += 1
    
    return sundays

print(count_sundays())
