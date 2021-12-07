import math as mt
def dist(x,y,x1,y1,x2,y2):
    dist=abs((x2-x1)*(y1-y)-(x1-x)*(y2-y1))/ \
         mt.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return dist 
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
    print("center of circle to point A =",
    d1,"\ncenter of circle to point B =",d2
    ,"\ncenter of circle to point C =",d3)
    dt1=dis_2points(x1,y1,x2,y2)
    dt2=dis_2points(x2,y2,x3,y3)
    dt3=dis_2points(x3,y3,x1,y1)
    if dt1>(dt2 and dt3):
        j=dt1
    elif dt2>(dt1 and dt3):
        j=dt2
    elif dt3>(dt1 and dt2):
        j=dt3
    if d1>=(j):
        return("CIRCLE OUTSIDE TRIANGLE")
    elif d2>=(j):
        return("CIRCLE OUTSIDE TRIANGLE")
    elif d3>=(j):
        return("CIRCLE OUTSIDE TRIANGLE")
    dist1=dist(cx,cy,x1,y1,x2,y2)
    dist2=dist(cx,cy,x2,y2,x3,y3)
    dist3=dist(cx,cy,x3,y3,x1,y1)
    if r<=(dist1 and dist2 and dist3):
        return ("CIRCLE INSIDE TRIANGLE")
    else:
        return ("CIRCLE OUTSIDE TRIANGLE")
        
    
print(circle_inside_triangel(0.1,0.1,0.5,0,0,1,0,1,1))
