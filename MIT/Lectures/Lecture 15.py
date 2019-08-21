import math
def addPoints(p1,p2):
    r=[]
    r.append(p1[0]+p2[0])
    r.append(p1[1]+p2[1])
    return r

#p=[1,2]
#q=[3,1]
#r=addPoints(p,q)
#print(r)

class cartesianPoint:
    pass

cp1=cartesianPoint() #Instance of this type
cp2=cartesianPoint() #Instance of this type
#Every instance has internal attributes
cp1.x=1.0 #Assign an x-value to cp1
cp1.y=2.0 #Assign a y-value to cp1
cp2.x=1.0 #Assign an x-value to cp2
cp2.y=3.0 #Assign a y-value to cp2

#print(cp1.y)

def samePoint(p1,p2):
    return (p1.x==p2.x) and (p1.y==p2.y)

#print(samePoint(cp1, cp2))

class cPoint:
    def __init__(self,x,y): #When cPoint is called, it is called with a specific set of arguments
    #init creates an instance
    #Self is used by init to refer to the instance
        self.x=x
        self.y=y
        self.radius=math.sqrt(self.x*self.x+self.y*self.y)
        self.angle=math.atan2(self.y,self.x)
    def cartesian(self):
        print(self.x, self.y)
        return (self.x, self.y)
    def polar(self):
        print(self.radius, self.angle)
        return (self.radius, self.angle)
    def __str__(self):
        #Gives a printed representation
        #Writing print(p) gives the return below
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __lt__(self,other):
        #Compares values
        print((self.x < other.x) and (self.y < other.y))
        return ((self.x < other.x) and (self.y < other.y))

#By saving p as a cPoint it becomes the Instance
#NOTE to get the value by using the in-written methods (.cartesian or .polar)
#remember to write it as: cPoint.polar() / cPoint.cartesian()
def DoAWholeBunch():
    p=cPoint(1.0,2.0)
    p2=cPoint(2.0,3.0)
    p.cartesian()
    p.polar()
    print("Changing the radius to 5.0")
    p.radius=5.0
    p.polar() #The polar form changes it's radius coordinate
    p.cartesian() #The Cartesian does NOT change
    p < p2
    print(dir(p))



class Segment:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def length(self):
        return math.sqrt( ((self.start.x - self.end.x) * (self.start.x - self.end.x)) \
        + ((self.start.y - self.end.y) * (self.start.y - self.end.y)))


p=cPoint(3.0,4.0)
p2=cPoint(5.0,7.0)
s1=Segment(p,p2)
print(s1.length())
