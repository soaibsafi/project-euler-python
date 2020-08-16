#PE-2
n1 = 1
n2 = 2
sum = 0
f = 0
while(True):
    f = n1+n2
    if f > 4000000:
        break
    if f%2 == 0:
        sum += f
    n1 = n2
    n2 = f
    print(sum)  
    
sum+2