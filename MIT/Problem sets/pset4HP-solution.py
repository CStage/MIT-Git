def nestEggFixed(salary,save,growthRate,years):
    money = [0]*years
    money[0] = salary*save*0.01
    for i in range(1,years):
        money[i] = money[i-1]*(1 + 0.01*growthRate) + salary*save*0.01
    return money
def nestEggVariable(salary, save, growthRates):
    money = [0]*len(growthRates)
    money[0] = salary*save*0.01
    for i in range(1,len(growthRates)):
        growthRate = growthRates[i]
        money[i] = money[i-1]*(1 + 0.01*growthRate) + salary*save*0.01
    return money
def postRetirement(savings,growthRates,expenses):
    money = [0]*len(growthRates)
    money[0] = savings*(1+0.01*growthRates[0]) - expenses
    for i in range(1,len(growthRates)):
        growthRate = growthRates[i]
        money[i] = money[i-1]*(1 + 0.01*growthRate) + -expenses
    return money
def findMaxExpenses(salary,save,preRetireGrowthRates,postRetireGrowthRates,epsilon):
    #Get the money untill you retire
    preRet = nestEggVariable(salary,save,preRetireGrowthRates)
    savings = preRet[-1]
    #make bottom and top guess for findMaxExpenses
    lowexp,highexp,centexp = 0,savings+epsilon,(savings+epsilon)/2
    remaining = 2*epsilon # just needs to be higher than epsilon to get into the loop
    while abs(remaining) > epsilon:
        #get the remaining in account with current guesses
        lowrem = postRetirement(savings,postRetireGrowthRates,lowexp)
        highrem = postRetirement(savings,postRetireGrowthRates,highexp)
        #Get the one closest to 0 and init for new search
        #print(f"using low: {lowexp} high: {highexp}")
        if abs(lowrem[-1]) <= abs(highrem[-1]):
            highexp = centexp
            remaining = lowrem[-1]
            print(f"Current expense is: {lowexp} getting ret of {remaining}")
        else:
            lowexp = centexp
            remaining = highrem[-1]
            print(f"Current expense is: {highexp} getting ret of {remaining}")
        centexp = lowexp + (highexp-lowexp)/2
    return centexp
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
testFindMaxExpenses()
