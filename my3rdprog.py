import numpy as np
import math 

# This c
def get_my_mean(x):
    n=len(x)
    y=1
    for i in range(0,n):
        print(x[i])
        y=x[i]*y
    p=pow(y,1/n)
    #p=y**(float(1/0.999))
    #p=np.power(y,float(1/0.999))
    return p
# B=np.random.random_integers(0,100,1000000)
#B=np.random.randint(0,100,1000000000)
a_mean=get_my_mean([1,2,3])
print(a_mean)
#print(np.mean(B))