# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:48:05 2020

@author: Soaib
"""


a=1
b=2
c=3

import numpy as np
import math
res = 0
for a in np.arange(1,500,1):
    for b in np.arange(a+1,500,1):
        for c in np.arange(b+1,500,1):
            if(a**2+b**2) == c**2 and a+b+c==1000:
                print(a,b,c)
                res = a*b*c
                break





def gcd(a, b):
    """"
        gcd(a,b) = gcd(a,b mod b)
    """
    x = y = 0
    if a>b:
        x = a
        y = b
    else:
        x = b
        y = a
    
    while x % y !=0:
        temp = x
        print(temp)
        x = y
        y = temp % x
    
    return y


""""
Euclid's Formula to calculate Phythagorian triples (primitive) :
    a = m^2-n^2
    b = 2*m*n
    c = a = m^2+n^2
    where m and n have opposite parity i.e. if m is obb, n is even
    & m, n are coprime i.e. they have no common factor grater than 1 -> (primitive Pythagorian triplet)
    
"""

a = b = c = 0
s = 1000
m = n = d = k = 0
found = False

max_limit = int(math.sqrt(s/2))+1
for m in np.arange(2, max_limit, 1):
    if (s/2) % m == 0:
        if m%2 == 0:
            k = m+1
        else:
            k = m+2
        while(k < 2*m and k <= s/(2*m)):
            
            if((s/(2*m)) % k == 0 and gcd(k,m)==1):
                d = s/2/(k*m)
                n = k - m
                a = d*(m*m - n*n)
                b = 2*d*m*n
                c = d * (m*m + n*n)
                found = True
                break
    if found:
        break