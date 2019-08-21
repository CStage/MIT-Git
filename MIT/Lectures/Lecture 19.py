import math, random, pylab

class Location(object):
    def __init__(self, x, y):
        self.x=float(x)
        self.y=float(y)
    def move(self, xc, yc):
        return Location(self.x+float(xc), self.y+float(yc))
    def getCoords(self):
        return self.y, self.x
    def getDist(self, other):
        ox, oy =other.getCoords()
        xDist=self.x-ox
        yDist=self.y-oy
        return math.sqrt(xDist**2+yDist**2)
class CompassPt(object):
    possibles=('N', 'S', 'E', 'W')
    def __init__(self, pt):
        if pt in self.possibles:
            self.pt=pt
        else:
            raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        if self.pt == 'N':
            return (0, dist)
        elif self.pt == 'S':
            return (0, -dist)
        elif self.pt == 'E':
            return (dist, 0)
        elif self.pt == 'W':
            return (-dist, 0)
        else:
            raise ValueError('in CompassPt.move')

class Field(object):
    def __init__(self, drunk, loc):
        self.drunk=drunk
        self.loc=loc
    def move(self, cp, dist):
        oldLoc=self.loc
        xc, yc = cp.move(dist)
        self.loc=oldLoc.move(xc, yc)
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk
    def isChute(self):
        x, y=self.loc.getCoords()
        return abs(x) - abs(y) == 0

class oddField(Field):
    def isChute(self):
        x, y = self.loc.getCoords()
        return abs(x) - abs(y) == 0
    def move(self, cp, dist):
        Field.move(self, cp, dist)
        if self.isChute():
            self.loc = Location(0, 0)


class Drunk(object):
    def __init__(self, name):
        self.name=name
    def move(self, field, cp, time=1): #time=1 is there if you DON'T give it a time
        if field.getDrunk()!=self:   #sort of like a default value
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(time):
            pt=CompassPt(random.choice(CompassPt.possibles))
            field.move(cp,1)

class UsualDrunk(Drunk):
    def move(self, field, dist=1):
        cp=random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), dist) #Note call to Drunk.move

class ColdDrunk(Drunk):
    def move(self, field, dist=1):
        cp=random.choice(CompassPt.possibles)
        if cp == 'S':
            Drunk.move(self, field, CompassPt(cp), 2*dist) #If the direction is South, then drunk takes 2 steps instead of 1
        else:
            Drunk.move(self, field, CompassPt(cp), dist)

class EWDrunk(Drunk):
    def move(self, field, time=1):
        cp=random.choice(CompassPt.possibles)
        while cp != 'E' and cp != 'W':
            cp=random.choice(CompassPt.possibles) #Drunk will ONLY move W or E
        Drunk.move(self, field, CompassPt(cp), time)

def performTrial(time,f):
    start=f.getLoc()
    distances=[0.0]
    for t in range(1, time+1):
        f.getDrunk().move(f) #Calling field in search of drunk. When drunk is found he is moved
        newLoc=f.getLoc()
        distance=newLoc.getDist(start)
        distances.append(distance)
    return distances

def performSim(time, numTrials, drunkType):
    distLists=[]
    for trial in range(numTrials):
        d = drunkType("Drunk" + str(trial))
        f=oddField(d, Location(0,0))
        distances=performTrial(time, f)
        distLists.append(distances)
    return distLists

def ansQuest(maxTime, numTrials, DrunkType, title):
    means=[]
    distLists=performSim(maxTime, numTrials, DrunkType)
    for t in range(maxTime + 1):
        tot=0.0
        for distL in distLists:
            tot+=distL[t]
        means.append(tot/len(distLists))
#        print("means", means)
#        print("tot", tot)
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel("avg. distance")
    pylab.xlabel("steps")
    pylab.title(title)

numSteps=500
numTrials=100
ansQuest(numSteps, numTrials, UsualDrunk, "UsualDrunk " + str(numTrials) + " Trials")
ansQuest(numSteps, numTrials, ColdDrunk, "ColdDrunk " + str(numTrials) + " Trials")
ansQuest(numSteps, numTrials, EWDrunk, "EWDrunk " + str(numTrials)+ " Trials")
pylab.show()
