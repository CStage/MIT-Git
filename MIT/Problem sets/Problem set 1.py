x=1
y=1000
itersLeft=y
#Repeat loop a set amount of time
while(itersLeft>0):
#Add 1 to original number, after testing if prime or not
    x=x+1
    if x>1:
#Check if dividing x by every number between 2 and x can ever yield the result:0
#if so, then that x is not a prime number
        for i in range(2,x):
            #print("i equals ", i)
            if (x % i) == 0:
                break
#Conversely, if division with all of these numbers yield no result of 0, then it
#is a prime number.
        else:
            print(x,"is a prime number")
            itersLeft=itersLeft-1
            if itersLeft==0:
                print("The 1000th prime number is: ", x)
