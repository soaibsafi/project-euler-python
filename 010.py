# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:08:44 2020

@author: Soaib
"""


import math

""""
Sieve of Atkin (modified upto 12):
    http://www.ams.org/mcom/2004-73-246/S0025-5718-03-01501-1/S0025-5718-03-01501-1.pdf 
    Algorithm:
       1. Create final list with 2,3,5
       2. Create a sieve list with an entry for each positive integer; all entries of this list should initially be marked non prime (composite)
       3. For each entry number n in the sieve list, with modulo-sixty remainder r (reminder when n is devided by 60):
           3.1. If r is 1, 13, 17, 29, 37, 41, 49, or 53:
               * flip the entry for each possible solution to 4*x*x + y*y = n
               * All numbers with module-sixty reminder 1, 13, 17, 29, 37, 41, 49, or 53 have a module-twelve reminder of 1 or 5
                 These number are prime if and only if the number of solutions to "4*x*x + y*y = n is odd" and number is square free (A square free integer is one which is not divisible by any perfect square than 1).
           3.2. If r is 7, 19, 31, or 43: 
               * flip the entry for each possible solution to 3*x*x + y*y
               * All numbers with module-sixty reminder 7, 19, 31, or 43 have a module-six reminder of 1
                 These number are prime if and only if the number of solutions to "3*x*x + y*y = n is odd" and number is square free
           3.3. If r is 11, 23, 47, or 59:
               * flip the entry for each possible solution to 3*x*x - y*y when x > y. 
               * All numbers with module-sixty reminder 11, 23, 47, or 59 have a module-twelve reminder of 11
                 These number are prime if and only if the number of solutions to "3*x*x - y*y = n is odd" and number is square free
           3.4. If r is something else, ignore it completely.
        4. Start with the lowest number in the sieve list.
        5. Take the next number in the sieve list still marked prime.
        6. Include the number in the results list.
        8. Square the number and mark all multiples of that square as non prime. Note that the multiples that can be factored by 2, 3, or 5 need not be marked, as these will be ignored in the final enumeration of primes.  
"""

def sieveOfAtkin(limit):
    is_prime = dict([(i, False)for i in range(limit+1)])
    
    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):
            n = 4*x*x + y*y
            if(n <= limit and (n%12 == 1 or n%12 == 5)):
               is_prime[n] = not is_prime[n]
               
            n = 3*x*x + y*y
            if(n<=limit and n%12==7):
                is_prime[n] = not is_prime[n]
                
            n = 3*x*x - y*y
            if((x>y) and n <= limit and n%12==11):
                is_prime[n] = not is_prime[n]
                
    for n in range(5, int(math.sqrt(limit))+1):
        if is_prime[n]:
            ik = 1
            while(ik*n*n <= limit):
                is_prime[ik*n*n] = False
                ik += 1
    
    """"
    Modification for problem 10
    """
    sum = 0
    for i in range(limit+1):
        if i in [0,1,4]: pass
        elif i in [2,3] or is_prime[i]: sum += i
        else:pass
    return sum

res = sieveOfAtkin(20)

