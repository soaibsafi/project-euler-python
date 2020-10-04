# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:33:34 2020

@author: Soaib
"""
import math

ones = [0, len('one'), len('two'), len('three'), len('four'), len('five'), len('six'), len('seven'), len('eight'), len('nine'), len('ten'), len('eleven'), len('twelve'), len('thirteen'), len('fourteen'), len('fifteen'), len('sixteen'), len('seventeen'), len('eighteen'), len('nineteen')]
tenth = [None, None, len('twenty'), len('thrity'), len('forty'), len('fifty'), len('sixty'), len('seventy'), len('eighty'), len('ninety') ]

def till99(n):
    if n < 20:
        return ones[n]
    return tenth[n//10 ] + ones[n%10]


def numberLength(n):
    if n<100:
        return till99(n)
    
    result = 0
    hundred = math.floor((n//100)%10)
    thousand = math.floor(n//1000)
    s = n % 100
    
    if n>999:
        result += till99(thousand) + len('thousand')
    if hundred != 0:
       result += ones[hundred] + len('hundred')     
    if s != 0:
        result += len('and') + till99(s)
    return result


letterscount = 0
for i in range(1001):
    #print(i)
    letterscount += numberLength(i)
    
print(letterscount)
