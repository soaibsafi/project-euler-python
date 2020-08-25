# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:38:24 2020

@author: soaibuzz
"""


""""
Brute force method takes a log time.
Here is the idea of mine:
    I have used Dynamic programming technique to store the  sequence which has been already calculated
    by means of so-called cache.
    Example:
        x=> 10 → 5 → 16 → 8 → 4 → 2 → 1
        y=> 13 → 40 → 20 → (10 → 5 → 16 → 8 → 4 → 2 → 1)
        y=>13 → 40 → 20 → x
"""
import operator
import time
start = time.time()
# Take a dictionary and initialize the keys & values with 0
# Keys will act as number and Values will stode the corresponding sequence number which is 'x' in previous example 
seq_dict = {x: 0 for x in range(1,1000001)}

seq_dict[1] = 1
seq_dict[2] = 2


for n in range(3, 1000000, 1):
    count = 0 #total sequence
    number = n #for every n
    while n>1:
        if n < number:
            seq_dict[number] = seq_dict[n] +count
            break
        if n%2 == 0:
            n = int(n/2)
            count +=1
        elif n%2 !=0:
            n = int(3*n+1)
            count += 1

longest_chain_number = max(seq_dict.items(), key=operator.itemgetter(1))[0]
print(longest_chain_number)


end = time.time()
print(end-start)
