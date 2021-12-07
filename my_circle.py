import math as mt
def my_circle(r):
    
    if r < 0:
        return ("input error")
    a=mt.pi * (r * r)
    return a

def diff_area(r1,r2):
    
    if r1 < r2:
        c=my_circle(r2) - my_circle(r1)
         
    elif r2 < r1:
        c=my_circle(r1) - my_circle(r2)
        
    elif r1==r2:
        c=my_circle(r1) - my_circle(r2)
        
    return c
print(diff_area(1,1.0000000000001))

    



