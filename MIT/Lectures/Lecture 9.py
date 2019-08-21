#Function that does binary search. Uses the splitting list method.
#s is the list
#e is the key
#first is the beginning index
#last is the ending index
#calls is how many iterations the program has run up to a certain point

def bSearch(s, e, first, last, calls):
    print(first, last, calls)
    if (last-first)<2:
        return s[int(first)] ==e or s[int(last)]==e
    mid=int(first+(last-first)/2)
    if s[int(mid)]==e:
        print("mid is: ", mid, "which is also the key.")
        return True
    if s[int(mid)]>e:
        return bSearch(s, e, first, mid-1, calls+1)
    return bSearch(s,e,mid+1,last, calls+1)

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

Ulist=[1,8,3,6,4]

def Search1(s,e):
    print(bSearch(s,e,0,len(s)-1,1))
    print("Search complete")


#Selection sort
#This method basically compares two numbers in the list in an attempt to determine
#which is larger and which is smaller. In our Ulist i starts out as being 1 and
#is being compared to j which is 8, 3, 6, and 4. 1 is smaller than all of them,
#so it's being placed at first index. minIndx now changes to [1] because, we've
#just determined that 1 is smaller than everything else, so the second smallest number
#should not also be placed at [0]

def selSort(L):
 for i in range(len(L) - 1):
    print(L)
    minIndx = i
    minVal= L[i]
    j = i + 1
    while j < len(L):
        if minVal > L[j]:
            minIndx = j
            minVal= L[j]
        j = j + 1
    temp = L[i]
    L[i] = L[minIndx]
    L[minIndx] = temp

#Bubble sort
#Pretty confusing at first, but see comments.

def BubbleSort(L):
    for j in range(len(L)): #Makes the program run as many times as there are elements in the list
        for i in range(len(L)-1): #Takes element at place i and compares to i+1
            if L[i]>L[i+1]:
                temp=L[i] #Saves the greater value in temp
                L[i]=L[i+1] #Puts the smaller value where the greater value was
                L[i+1]=temp #Puts the greater value where the smaller value was
        print(L)

BubbleSort(Ulist)

#Same as bubble sort but will STOP if no swaps have been made, because then we
#know that everything is sorted
def BubbleSortSwap(L):
    Swapped=True
    while Swapped:
        Swapped=False
        for i in range(len(L)-1): #Takes element at place i and compares to i+1
            if L[i]>L[i+1]:
                temp=L[i] #Saves the greater value in temp
                L[i]=L[i+1] #Puts the smaller value where the greater value was
                L[i+1]=temp #Puts the greater value where the smaller value was
                Swapped=True
        print("Swaplist", L)

BubbleSortSwap(Ulist)
