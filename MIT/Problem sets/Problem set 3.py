def StringScript(string1,string2):
    import string
    print(string1.find(string2))


target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



# these are some example strings for use in testing your code

#  target strings


#Problem 1.
    #Write two functions, called countSubStringMatch and countSubStringMatchRecursive that
    #take two arguments, a key string and a target string. These functions iteratively and recursively count
    #the number of instances of the key in the target string. You should complete definitions for
    #def countSubStringMatch(target,key):
    #and
    #def countSubStringMatchRecursive (target, key):
    #Place your answer in a file named ps3a.py

def countSubStringMatch():
    import string
    target=str(input("Give me a string you wanna search: "))
    key=str(input("Give me the key you wanna search for: "))
    count=0
    for i in target:
        if i==key:
            count=count+1
        else:
            count=count
    print("There are ",count, key, "'s in", target)

def countSubStringMatchRecursive(sentence,key):
    print("sentence", sentence)
    if len(sentence)>=2:
        mid=int((len(sentence))/2)
        return countSubStringMatchRecursive(sentence[:mid],key) + countSubStringMatchRecursive(sentence[mid:],key)
    if len(sentence)==1 and sentence[0]==key:
        return 1
    else:
        return 0
#Test=["Banana","apple","Banana","Banana","coconut","Tanzania"]
#print(countSubStringMatchRecursive(Test, "Banana"))


def subStringMatchExact(target,key):
    count=0
    keycount=0
    results=[]
    for i in target:
        if i==key:
            count+=1
        results=[target.find(key) for i in target]
        keycount+=1
    print(keycount)
    print(results)
    print(count)




target1="atgacatgcacaagtatgcat"
target2="atgaatgcatggatgtaaatgcag"

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

print(subStringMatchExact(target1,key10))
