import math as mt
def dis_2points(x1,y1,x2,y2):
    x=x1-x2; y=y1-y2
    d=mt.sqrt((x*x)+(y*y))
    return d
def circle_inside_triangel(r,cx,cy,x1,y1,x2,y2,x3,y3):
    if r<=0 :
        return ("error radius input")
    d1=dis_2points(cx,cy,x1,y1)
    d2=dis_2points(cx,cy,x2,y2)
    d3=dis_2points(cx,cy,x3,y3)
    dt1=dis_2points(x1,y1,x2,y2)
    dt2=dis_2points(x2,y2,x3,y3)
    dt3=dis_2points(x3,y3,x1,y1)
    print(dt1,dt2,dt3)
    if dt1>(dt2 or dt3):
        j=dt1
    elif dt2>(dt1 or dt3):
        j=dt2
    elif dt3>(dt1 or dt2):
        j=dt3
    if d1>=(j):
        return("circle out")
    elif d2>=(j):
        return("circle out")
    elif d3>=(j):
        return("circle out")
    dist1 = abs((x2-x1)*(y1-cy)-(x1-cx)*(y2-y1))/ \
         mt.sqrt(((x2-x1)**2)+((y2-y1)**2))
    dist2 = abs((x3-x2)*(y2-cy)-(x2-cx)*(y3-y2))/ \
         mt.sqrt(((x3-x2)**2)+((y3-y2)**2))
    dist3 = abs((x1-x3)*(y3-cy)-(x3-cx)*(y1-y3))/ \
         mt.sqrt(((x1-x3)**2)+((y1-y3)**2))
    if r<=(dist1 or dist2 or dist3):
        return ("circle in")
    else:
        return ("circle out")
        
    
print(circle_inside_triangel(0.1,0.1,0.5,0,0,1,0,1,1))

    