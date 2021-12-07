import math as mt
from typing import Any
def convert_radian2degree(x):
    return (x*(180/mt.pi))

def triangel_a_b_c(x,y,z=0):
    if y==0:
        alf=convert_radian2degree(mt.asin(x/z))
        return(alf)
    elif x==0:
        alf=convert_radian2degree(mt.acos(y/z))
        return(alf)
    elif z==0:
        alf=convert_radian2degree(mt.atan(x/y))
        return(alf)
print("the angel in degree is = ",triangel_a_b_c(0,640,920))
#print(triangel_a_b_c(0,640,420))
    