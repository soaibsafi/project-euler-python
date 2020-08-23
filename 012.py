# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 08:17:21 2020

@author: Soaib
"""

import math

""""
Calculate the number of divisors of integer n
"""
def divisor(n):
    limit = int(math.sqrt(n))
    divisor_list = []
    
    for i in range(1, limit+1, 1):
        if n%i == 0:
            divisor_list.append(i)
            if i != n/i:
                divisor_list.append(n/i)
    return len(divisor_list)
            

""""
A number 'x' is triangle number if and only if '8*x+1' is a square.
This can be proved by solving the equation => x = n*(n+1)/2

Lambda:
    1. Multiply x by 8 and subtract 1
    2. Find the square root of that number -> (a**0.5)
    3. Subtract it by 1 and devide it by 2
"""
is_Trienguler = lambda x: (0.5*((8*x+1) ** 0.5-1)).is_integer()


""""
Calculate the last term of the series adding up to the triangle number 
"""
def seriesLast(n):
    if is_Trienguler(n):
        return int(math.sqrt(2*n))
    else:
        return None

""""
Using Prime decomposition: Every integer N is the product of power of prime number.
    N = product(i=1 -> k) Pi**mi
    If N is a power of a prime, N = P**a, then it has α + 1 factors: -> 1, p, …, p**(α-1), pα
    Then the divisors would be: product(i=1 -> k) mi+1
Example:
    Find the smallest number with 500 divisors
    -------
    500 = 2*2*5*5*5
    Now, applying the biggest mi to the smallest prime
    => 2**(5-1) * 3**(5-1) * 5**(5-1) * 7**(2-1) * 11**(2-1)
    => 2**4 * 3**4 * 5**4 * 7 * 11
"""
checkdivisor = 2**4 * 3**4 * 5**4 * 7 * 11


while not is_Trienguler(checkdivisor):
    checkdivisor += 1
    
seriesLastTerm = seriesLast(checkdivisor)

while divisor(checkdivisor) <= 500:
    checkdivisor += (seriesLastTerm+1)
    seriesLastTerm += 1
    
print(checkdivisor)