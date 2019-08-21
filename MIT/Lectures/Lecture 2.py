#x=15
#y=5
#z=11
#print(x,y,z)

#if x<y:
#    if x<z: print(" x is least")
#    else: print ("z is least")
#elif y<x:
#    if y<z: print("y is least")
#    else: print("z is least")
#else: print("y is least")

y=0
x=100
itersLeft=x
while(itersLeft>0):
    y=y+x
    itersLeft=itersLeft-1
    print("y=", y, "itersLeft= ", itersLeft)
print(y)
