import numpy as np
def matrix(n):
    c=[[1,1],[1,0]]
    a=[[1,1],[1,0]]
    fib=[3,2]
    c=np.mat(c)
    a=np.mat(a)
    if n==1:
        return fib[1]
    if n==2:
        return fib[0]
    for x in range(n-3):
        c*=a
    c=np.array(c)
    sum=0
    for i in range(2):
        sum+=c[0][i]*fib[i]
    return sum
c=int(raw_input("Enter n: "))
while(c!=-1):
    print matrix(c)
    c=int(raw_input("Enter n: "))