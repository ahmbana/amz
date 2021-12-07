import math as mt
def convert_radian2degree(x):
    return (x*(180/mt.pi))
def circle(r1,xp1,yp1,r2,xp2,yp2):
    if (r1<0) | (r2<0):
        return ("error radius input")
    if r1<r2:
        xp=xp1-xp2
        yp=yp1-yp2
        d=mt.sqrt((xp*xp)+(yp*yp))
        Dx=xp+((xp/d)*r1)
        Dy=yp+((yp/d)*r1)
        D=mt.sqrt((Dx*Dx)+(Dy*Dy))
        if D<=r2 :
            alf=convert_radian2degree(mt.acos(((Dx*1)+(Dy*0))/D))
            print(alf)
            return ("circle-1 is inside circle-2")
        else:
            return ("independent circles")
    elif r2<r1:
        xp=xp2-xp1
        yp=yp2-yp1
        d=mt.sqrt((xp*xp)+(yp*yp))
        Dx=xp+((xp/d)*r2)
        Dy=yp+((yp/d)*r2)
        D=mt.sqrt((Dx*Dx)+(Dy*Dy))
        if D<=r1:
            alf=convert_radian2degree(mt.acos(((Dx*1)+(Dy*0))/D))
            print(alf)

            return ("circle-2 inside circle-1")

        else:
            return ("independent circles")
   

print(circle(1,-1,-1,3,0,0))
