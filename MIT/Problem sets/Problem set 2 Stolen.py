n = 1     # n starting from 1
count = 0 # Count + 1 everytime we find an impossible value.
              # Reset = 0 after a non-possible value.
notPossibleValue = () #This is a Tuple that eventually saves all the values that are impossible
while True:
    ind = 0 # becomes 1 if int solutions were found
    for c in range (0,n//20+1): #Establishing the largest possible amount of whole
                                #20-piece boxes you can buy + 1 (to establish
                                #an upper-bound that is definitely too high)
        if ind == 1: break
        for b in range (0,n//9+1): #Establishing the largest possible amount of
                                   #whole 9-piece boxes you can buy + 1
            if ind == 1: break
            for a in range (0, n//6+1):     #Establishing the largest possible amount of whole 6-pieces you can buy+1
                if (n) == (20*c+b*9+a*6):   #Tests if n can be equal to any combination of the diophantine equation with positive integers
                        count+=1 #IF above comment can be true, then 1 is added to Count
                        ind=1    #And ind is set equal to 1, which will cause the loop to Break
                        #print ('n=', n, a,b,c, 'count', count)
                        break # Break out of "a" loop
#Next if-condition is only reached for values of n that are not equal to a combination of the diophantine euation wtih positive integers
#This will also reset the COUNT to be 0, so we can start counting the succession over (Will make sense in a bit)
#Lastly, the impossible n-value is saved in a tuple

    if ind == 0:
        count = 0
        notPossibleValue=notPossibleValue+(n,)
        #could also be written as: notPossibleValue+=(n,)
        # print notPossibleValue, 'count', count

#When we reach 6 possible values in a row, then every value onwards will be possible
#Therefore, when COUNT reaches 6, the last variable stored in notPossibleValue will be the largest impossible value
#The if-condition prints all impossible values and highlights the largest impossible value
#NOTE since this if-condition is at the same indent as WHILE then BREAK will cause the script to stop, with the loop stopping
    if count == 6:
        print('The largest number of McNuggets that cannot be bought in exact quantity is', notPossibleValue[-1])
        print(notPossibleValue)
        break
#After breaking out of the a,b,c-loop 1 is added to n, to make sure that we keep counting
#1 is added continuously until we've reached a count of 6
    n+=1
