#Perfect square root

x=9
ans=0
while ans*ans<x:
    ans=ans+1
print(ans, "is it")


#y=10
#i=1
#while i<=y:
#    if y%i==0:
#        print(i, "is a divisor")
#        i=i+1
#    else:
#        print(i, "is not a divisor")
#        i=i+1


y=10
for i in range(1,y):
    if y%i==0:
        print(i, "is a divisor")
#Notice that using For i in Loop we don't have to increment
#In the previous attempt we wrote: i=i+1, that is not necessary here
#The range() determines where to start and the first number it shouldn't include
#it goes up to, but doesn't include, y.


#Using a Tuple
z=100
divisors = ()
for i in range(1,z):
    if z%i==0:
        divisors=divisors+(i,)

#Using a string as Tuple
s1="Jeg er sej"
s2="og jeg elsker flæskesteg"

print(s1, s1[0], s1[2], s1[9])
print(s2[2:10])

sumdigits=0
for c in str(1952):
    sumdigits=sumdigits+int(c)
print(sumdigits)
