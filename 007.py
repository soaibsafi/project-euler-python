# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:58:41 2020

@author: Soaib
"""
def is_prime(x):
    if x%2 == 0:
        return False
    for i in range(3, x, 2):
        if x%i == 0:
            return False
    return True

prime_count = 1

i=3
while True:
    if prime_count == 10001:
        break
    if is_prime(i):
        print(i)
        prime_count += 1
    i += 1

res = i-1