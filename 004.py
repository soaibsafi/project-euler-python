# PE - 4

import numpy as np
def is_palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig = num%10
        rev = rev*10+dig
        num = num//10
        
    if temp == rev:
        return True
    return False

largest_palindromes = []
for i in np.arange(100, 1000, 1):
    for j in np.arange(100, 1000, 1):
        mul = i*j
        if(is_palindrome(mul)):
            largest_palindromes.append(mul)
            
max(largest_palindromes)