# Problem Set 4
# Name:
# Collaborators:
# Time:

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    Results=[]
    for i in range(years+1):
        if i==0:
            Results.append(salary*save*0.01)
            #print("First results:", Results)
        else:
            Results.append(Results[i-1]*(1+0.01*growthRate)+salary*save*0.01)
            #print("other results: ", Results)
    print(Results)

#nestEggFixed(10000,10,15,5)

"""
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.


def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#


    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
def nestEggVariable(salary, save, growthRates):
    Results=[]
    for i in range(len(growthRates)):
#        print("i", i)
        if i==0:
            Results.append(salary*save*0.01)
#            print("results:", Results)
        else:
            Results.append(Results[i-1]*(1+0.01*growthRates[i])+salary*save*0.01)
#            print("GrowthRates[i]", growthRates[i])
#            print("other results", Results)
#    print("FINAL", Results)
    return Results

list=[3,4,5,0,3]
#nestEggVariable(10000,10,list)


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    Results=[]
    for i in range(len(growthRates)):
        #print("i", i)
        if i==0:
            Results.append(savings*(1+0.01*growthRates[i])-expenses)
            #print("GrowthRates[i]", growthRates[i])
            #print("results:", Results)
        else:
            Results.append(Results[i-1]*(1+0.01*growthRates[i])-expenses)
            #print("GrowthRates[i]", growthRates[i])
            #print("other results", Results)
#    print("FINAL", Results)
    return Results

growthRates1=[10,5,0,5,1]
#postRetirement(100000, growthRates1, 30000)

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    preRet=nestEggVariable(salary, save, preRetireGrowthRates)
    savings=preRet[-1]
    #Using binary search to make guesses about findMaxExpenses
    lowexp=0
    highexp=savings+epsilon
    centexp=(savings+epsilon)/2
    remaining=2*epsilon #Used to get into the loop. Interesting concept

    while abs(remaining)>epsilon:
        #Gets the remaining money in the account with current quesses
        #The low guess
        lowrem=postRetirement(savings, postRetireGrowthRates, lowexp)
        #The high guess
        highrem=postRetirement(savings, postRetireGrowthRates, highexp)
        #We keep whichever is closest to 0 and then keep going.
        #Keep in mind that goal of this program is to find expenses such that
        #amount left in account is 0
        #If the lower guess is lower or equal to the higher guess, then we cut
        #the line in half and make the high expense equal to the center expense
        if abs(lowrem[-1]) <= abs(highrem[-1]):
            highexp=centexp
            remaining=lowrem[-1]
            print("Current expense is:", lowexp, "getting ret of", remaining)
        else:
            lowexp=centexp
            remaining=highrem[-1]
            print("Current expense is:", highexp, "getting ret of", remaining)
        centexp=lowexp + (highexp-lowexp)/2
    return centexp
    print(preRet, savings)




def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
testFindMaxExpenses()
