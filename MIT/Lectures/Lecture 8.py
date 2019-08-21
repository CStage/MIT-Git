#Search allows me to search for a key within a sorted list
#s is the list and e is what we search for
#i is the index, and the code basically says that while i is shorter than the the
#length of the list and no answer has been given yet (whether true or false)
#then it should keep looking through s to see if it can find e.
#i=0 means that we START looking at index 0
#For every run-through where we don't find what we need, we look for the key at
#index that is 1 higher than the previous

def Search(s,e):
    answer=None
    i = 0
    numCompares=0
    while i < len(s) and answer==None:
        numCompares+=1
        if e==s[i]:
            answer=True
        elif e<s[i]:
            answer=False
        i+=1
    print(answer,numCompares)

#If you are working with a sorted list it is a great idea to make the search START
#at the middle of the list. That way you can throw half the list out at each
#run-through. Basically, using a log-function is worth way more for you.

def bSearch(s, e, first, last):
    print(first, last)
    if (last-first)<2:
        return s[int(first)] ==e or s[int(last)]==e
    mid=first+(last-first)/2
    if s[int(mid)]==e:
        return True
    if s[int(mid)]>e:
        return bSearch(s,e, first, mid-1)
    return bSearch(s,e,mid+1,last)

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def Search1(s,e):
    print(bSearch(s,e,0,len(s)-1))
    print("Search complete")

Search1(list,13)
