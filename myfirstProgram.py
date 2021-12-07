import numpy as np
from numpy.core import machar
from numpy.lib.twodim_base import mask_indices


np.abs(-10)


print("Hallo World")

def myABS(input_value):
    
    if(input_value < 0):
        print("less than zero")
        input_value = -input_value
    
    return input_value
    
print(np.abs(-3.14))

# print(myABS("ak"))

print(np.abs("ak"))
