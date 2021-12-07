
import numpy as np

def get_my_min(a1,a2,a3):
    if((a1<a2) & (a1<a3)):
        return a1
    elif((a2<a1) & (a2<a3)):
        return a2
    elif((a3<a1) & (a3<a2)):
        return a3 
    else:
        return("rag3 ala7' ely wara")

def print_my_vec(x,i):
    #print(len(x))
    #print(x[i])
    for k in range(0,len(x)):
        print("k=",k)
        print(x[k])

A=[1,2,5,9,5,4,8,6,200,10]
print_my_vec(A,3)
#print_my_vec(np.random(10),3)
B=np.random.random_integers(0,100,1000000)
#print(np.random.random_integers(0,100,1000000))
print_my_vec(B,3)