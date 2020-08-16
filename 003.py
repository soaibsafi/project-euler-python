# PE-3
import numpy as np
import math

n = 600851475143
largest_factor = 0
while(n%2 ==0):
    largest_factor = 2
    n /=2

for i in np.arange(3, math.sqrt(n), 2):
    if(n%i == 0):
        largest_factor = i
        n /= i;
        
print(largest_factor)
