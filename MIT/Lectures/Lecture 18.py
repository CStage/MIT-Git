from pylab import *
import random

#plot([1,2,3,4])
#plot([5,6,7,8])

#plot([1,2,3,4], [1,4,9,16]) #First list is x-values, second list is y-values
#figure() #Says: "Create a new figure"
#plot([1,2,3,4], [1,4,9,16], "go")
#title("Earnings")
#xlabel("Days")
#ylabel("Dollars")
#figure()
#xAxis = array([1,2,3,4]) #Applying array to a list, turns list in to an array (matrix)
#print(xAxis)
#test=arange(1,5)
#print(test)
#print(test==xAxis) #Instead of comparing if two lists are EXACTLY equal. It compares
                   #whether or not every element in list 1 is equal to list 2 at
                   #given index
#yAxis=xAxis**3
#plot(xAxis, yAxis, "ro")

figure()
vals=[]
dieVals=[1,2,3,4,5,6]
for i in range(10000):
    vals.append(random.choice(dieVals)+random.choice(dieVals))
hist(vals,bins=11)
show()




















show()
