def SquareRootBi():
    x=float(input("What do you want the square root of? "))
    epsilon=float(input("How precise do you need it to be? "))
    """Assumes x >= 0 and epsilon > 0"""
    """ Return y s.t. and y*y is within epsilon of x"""
    assert x>=0, "x must be non-negative. Not " + str(x)
    assert epsilon>0, "epsilon must be higher than 0. Not " + str(epsilon)
    low=0
    high=max(x,1)
    guess=(low+high)/2.0
    ctr=1
    while(abs(guess**2-x)>epsilon and ctr<=100):
        if guess**2<x:
            low=guess
        else:
            high=guess
        guess=(low+high)/2.0
        ctr+=1
    assert ctr<=100, "iteration count exceeded"
    print("Bi method. Iteration count: ", ctr, "Estimate: ", guess)
    return guess

SquareRootBi()
