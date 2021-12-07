import math as mt

def circle(r1,xp1,yp1,r2,xp2,yp2):
    if (r1<0) | (r2<0):
        return ("error radius input")
    if r1<r2:
        xp=xp1-xp2
        yp=yp1-yp2
        d=mt.sqrt((xp*xp)+(yp*yp))
        if r2>d:
            return ("circle-1 is inside circle-2")
        else:
            return ("independent circles")
    elif r2<r1:
        xp=xp2-xp1
        yp=yp2-yp1
        d=mt.sqrt((xp*xp)+(yp*yp))
        if r1>d:
            return ("circle-2 inside circle-1")   
        else:
            return ("independent circles")
print(circle(1,2.9,0,3,0,0))
    
