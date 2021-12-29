# ******* Signature: Dawwas **********
def my_fac(n):
    if (n==1) | (n==0):
        return 1
    if (n>1):
        # Recursive Magic
        return n*my_fac(n-1)
    else:
        # "!" only defined for n >=0 
        raise ValueError



# Test
print(my_fac(5))