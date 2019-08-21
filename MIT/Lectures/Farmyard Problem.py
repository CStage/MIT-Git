#You have 20 heads and 56 legs. How many chickens and how many pigs do you have?
#numP+numC=20, 4*legP+2*legC=56
#Enumerating and checking all possible results of this is called: Brute force algorithm

def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads+1):
        for numSpiders in range(0,numHeads-numChicks+1):
            numPigs=numHeads-numChicks-numSpiders
            totLegs=4*numPigs+2*numChicks+8*numSpiders
            if totLegs==numLegs:
                return (numPigs, numChicks, numSpiders)
    return (None, None, None)

def BarnYard():
    heads=int(input("How many heads: "))
    legs=int(input("How many legs: "))
    pigs, chickens, spiders = solve (legs, heads)
    if pigs==None:
        print("There is no solution")
    else:
        print("No. of pigs: ", pigs)
        print("No. of chickens: ", chickens)
        print("No. of Spiders: ", spiders)



def solve2(numLegs, numHeads):
    solutionfound=False
    for numChicks in range(0, numHeads+1):
        for numSpiders in range(0,numHeads-numChicks+1):
            numPigs=numHeads-numChicks-numSpiders
            totLegs=4*numPigs+2*numChicks+8*numSpiders
            if totLegs==numLegs:
                print('Number of pigs: ' + str(numPigs) + ',',)
                print('Number of chickens: '+str(numChicks)+',',)
                print('Number of spiders:', numSpiders)
                solutionFound = True
    if not solutionFound: print ('There is no solution.')


def isPalindrome(s):
    """Evaluates whether or not a string is a palindrome"""
    if len(s)<=1: return True
    else: return s[0]==s[-1] and isPalindrome(s[1:-1])

print(isPalindrome("abcdcba"))

def fib(x):
    if x==0 or x==1: return 1
    else: return fib(x-1) + fib(x-2)

print(fib(30))
