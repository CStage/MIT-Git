list1=[3,12,17,24]
list2=[1,2,4,30]
list3=[1,4,3,6,5,2,8,7]

def merge(left,right):
    """Assumes left and right are sorted lists.
Returns a new sorted list containing the same elements
as (left + right) would contain."""
    result=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while (i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return result



#MergeSort
#We want to merge two sorted lists
#Divide lists in half, and keep dividing in half until we have a bunch of lists
#of length=1, then merge the sublists.



def MergeSort(L):
    '''Returns a sorted list of one list'''
    print(L)
    if len(L)<2:
        return(L[:]) #L[:] is jus the list as it is
    else:
        middle=len(L)/2
        left=MergeSort(L[:(int(middle))])
        right=MergeSort(L[(int(middle)):])
        together=merge(left,right)
        print("Merged ", together)
        return together


#Hashing
#Create
#Makes a list containing random integers between 0 and 9
def create(smallest, largest):
    intSet=[]
    for i in range(smallest, largest+1):
        intSet.append(None)
    print(intSet)
    return intSet


create(0,9)

def insert(intSet,e):
    intSet[e]=1

def member(intSet,e):
    return intSet[e]==1


def hashChar(c):
# c is a char
# function returns a different integer in the range 0-255
# for each possible value of c
    print(ord(c))
    return ord(c)

def cSetCreate():
    cSet = []
    for i in range(0, 255):
        cSet.append(None)
    return cSet

def cSetInsert(cSet, e):
    cSet[hashChar(e)] = 1

def cSetMember(cSet, e):
    return cSet[hashChar(e)] == 1


#This will try to turn the value into a float. If it works, then it moves on,
#if it doesn't (if the val is a string), then it gives an error, so we can try again
#that is a handled exception.
def ReadFloat(requestMSG, errorMSG):
    while True:
        val=input(requestMSG)
        try:
            val=float(val)
            return val
        except:
            print(errorMSG)

ReadFloat("Gimme", "No")
