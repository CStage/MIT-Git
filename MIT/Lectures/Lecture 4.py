def sqrt(x):
    """Returns the sqrt of x if x is a perfect square, otherwise returns None"""
    ans=0
    if x>=0:
        while ans*ans<x: ans=ans+1
        if ans*ans != x:
            print(x, " is not a perfect square!")
            return None
            #Note, it returns ans, but it does not print it!!
        else: return ans
    else:
        print(x, " is a negative number!")
        return None

print(sqrt(16)+sqrt(16))

def f(x):
    x=x+1
    return x
print(f(16))
test=sqrt(16)
#Test to see if test contains a value or simply has a return of 'None', in which
#case the print will say true
print(test==None)
test=sqrt(34)
#Same as before but with differnt sqrt
print(test==None)
