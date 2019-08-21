def showDicts():
    EtoF={"one":"un","soccer":"football","never":"jamais"}
    print (EtoF["never"])
    input()
    #print(EtoF[0])
    print(EtoF)
    input()
    NtoS={1:"one",2:"two","one":1,"two":2}
    print(NtoS)
    print(NtoS.keys())
    input()
    print(NtoS.keys())
    input()
    del(NtoS["one"])
    print(NtoS)
    input()

showDicts()


def Rhyp():
#I cannot for the life of me make this disregard integers... Ask Henrik maybe?
    import math
    import numbers
#Get base
    inputOK = False
    while not inputOK:
        try:
            base=float(input("Enter base: "))
            print("Yup, that is a float")
            inputOK=True
        except ValueError:
            print("That is not a float")
    #Get Height
    inputOK = False
    while not inputOK:
        try:
            height=float(input("Enter height: "))
            print("Yup, that is a float")
            inputOK=True
        except ValueError:
            print("That is not a float")

    hyp = math.sqrt(base*base + height*height)

    print('Base: '+str(base)+',height: '+str(height)+', hyp: '+ str(hyp))


#This code will find the result of a to the power of b in an iterative way
#It's not the most efficient method, but it gets the job done.
def exp1(a,b):
    ans=1 #Had ans=0 program would run forever
    while(b>0):
        ans*=a
        b-=1
    return ans

#Pretty much same idea as before, except instead of a while loop we use an if:
#With a return to the original function with a value-change
#Only when b==1 do we completely exit the loop RECURSIVE program
def exp2(a,b):
    if b==1:
        return a
    else:
        return a*exp2(a,b-1)

#This program cuts the problem in half if the exponent is even
#If the exponent is an even number, then:
#3^4=9^2
#So we can basically halve the problem until we arrive at b==1

def exp3(a,b):
    if b==1:
        return a
    if (b%2)*2==b: #Tests if b is even
        return exp3(a*a,b/2)
    else: #In case b is even, then this program runs like exp2()
        return a*exp3(a,b-1)

#This basically just does multiplication by saying that I want x=x+1 for every
#integer up until m, and I want to do that operation n times.
#Notice that it goes through loop j m*n times. In the case of n=3, m=4
#3*4=12
def g(n,m):
    x=0
    for i in range(n):
        for j in range(m):
            x+=1
    return x


#Towers is based on the idea of the monks in Hanoi trying to move disks from one
#tower to another while keeping the lowest disk at the bottom at all times.
def Towers(size, fromStack, toStack, spareStack):
    if size==1:
        print("Move disk from: ", fromStack, "to: ", toStack)
    else:
        Towers(size-1, fromStack, spareStack, toStack)
        Towers(1, fromStack, spareStack, toStack)
        Towers(size-1, spareStack,toStack,fromStack)
