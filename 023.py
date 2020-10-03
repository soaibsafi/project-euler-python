# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:20:15 2020

@author: Soaib
"""

""""
Problem:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt

# Get all the divisor using prime factorization
def getAllDivisor(n):
    divisor = [1]
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            divisor.extend([i,n/i])
    return list(set(divisor))
            
# List to store all the abandant numbers
abandantNumbers = list()

# Generating all the abandant numbers
for i in range(12,28123):
	if sum(getAllDivisor(i))>i:
		abandantNumbers.append(i)
 
# Let us assume all the numbers are not sum_of_abandant_numbers
nonAbandantSum = [x for x in range(28123)]
        
# Generatiing sum of two abandant numbers
for i in range(len(abandantNumbers)):
    for j in range(i, 28123):
        if abandantNumbers[i] + abandantNumbers[j] < 28123:
            # neglecting the value which can ba written as sum of two abandant numbers
            nonAbandantSum[abandantNumbers[i]+abandantNumbers[j]] = 0
        else:
            break

print(sum(nonAbandantSum))

