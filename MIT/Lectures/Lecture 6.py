#Do the SquareRootNR thing
def SquareRootNR():
    x=float(input("What do you want the square root of? "))
    epsilon=float(input("How precise do you need it to be? "))
    """Assumes x >= 0 and epsilon > 0"""
    """ Return y s.t. and y*y is within epsilon of x"""
    assert x>=0, "x must be non-negative. Not " + str(x)
    assert epsilon>0, "epsilon must be higher than 0. Not " + str(epsilon)
    low=0
    guess=x/2.0
    diff=guess**2-x
    ctr=1
    while abs(diff)> epsilon and ctr <=100:
        guess=guess-diff/(2.0*guess)
        diff=guess**2-x
        ctr+=1
        assert ctr <= 100, 'Iteration count exceeded'
    print('NR method. Num. iterations:', ctr, 'Estimate:', guess)
    return guess

SquareRootNR()
