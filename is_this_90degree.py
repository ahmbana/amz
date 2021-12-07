import math as mt

def conv_radian2dgree(x):
    return (x*(180/mt.pi))

def is_this_90degree(x1,y1,x2,y2,x3,y3):
    x12=x1-x2;y12=y1-y2
    x13=x1-x3;y13=y1-y3
    x23=x2-x3;y23=y2-y3
    
    d12=mt.sqrt((x12*x12)+(y12*y12))
    d13=mt.sqrt((x13*x13)+(y13*y13))
    d23=mt.sqrt((x23*x23)+(y23*y23))
    
    alfa=conv_radian2dgree(mt.acos(((x12*x13)+(y12*y13))/(d12*d13)))
    beata=conv_radian2dgree(mt.acos(((x12*x23)+(y12*y23))/(d12*d23)))
    gama=conv_radian2dgree(mt.acos(((x13*x23)+(y13*y23))/(d13*d23)))
     #schwerpunkt
    Sx=(1/3)*(x1+x2+x3);Sy=(1/3)*(y1+y2+y3)
    print("Schwerpunkt","X=",Sx,"Y=",Sy)
    if (alfa==90)|(beata==90)|(gama==90):
        return("True")
    else:
        return("False")
    
print("90 degree angel is",is_this_90degree(1,0.1,0,0,1,1))