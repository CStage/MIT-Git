# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:
import ps11_visualize
import math
import random
import pylab

# === Provided classes


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
#        print("oldx", old_x, "delta_x", delta_x)
        new_y = old_y + delta_y
#        print("oldy", old_y, "delta_y", delta_y)
        return Position(new_x, new_y)
#    def __eq__(self,other):
#        return self.x==other.x and self.y==other.y
#    def __hash__(self):
#        return hash((self.x, self.y))
    def __str__(self):
        return "Position with coordinates [" + str(self.x) + "," + str(self.y) + "]"

# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        assert 0<width
        assert 0<height
        self.width=int(width)
        self.height=int(height)
        self.cleanTiles={}

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        intposition=int(pos.x), int(pos.y)
        self.cleanTiles[intposition]=self.cleanTiles.get(intposition,0)+1

#        print(cleanTiles)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        questionedPosition=Position(int(m), int(n))
        if (m, n) in self.cleanTiles:
            return True
        return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return int(self.width*self.height)
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here

        return len(self.cleanTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        p=Position(random.randint(0,self.width), random.randint(0,self.height))
#        print(p)
        return p

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if 0<=pos.x<=self.width and 0<=pos.y<=self.height:
            return True
        else:
            return False

        # TODO: Your code goes here
p1=Position(2,1)
p2=Position(2,3)
g=RectangularRoom(5,5)
#g.cleanTileAtPosition(p1)
#print(g.cleanTileAtPosition(p1))
#g.cleanTileAtPosition(p2)
g.getRandomPosition()
g.isPositionInRoom(Position(2,1))
#print(g.getNumCleanedTiles())
#print(g.isPositionInRoom(p1))
class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.room=room
        self.speed=speed
        self.d=random.randint(0,360)
        self.p=room.getRandomPosition()

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
#        print(self.p)
        return self.p
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
#        print(self.d)
        return self.d
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.p=position
        return self.p
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.d=direction
        return self.d
#robot=BaseRobot(g, 1)
#robot.getRobotPosition()
#robot.getRobotDirection()
#robot.setRobotPosition(Position(2,1))
#robot.getRobotPosition()

class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        AtWall=False

        while not AtWall:
             currentPosition=self.getRobotPosition()
             nextPosition=currentPosition.getNewPosition(self.getRobotDirection(), self.speed)
             if self.room.isPositionInRoom(nextPosition):
                 self.p=nextPosition
                 self.room.cleanTileAtPosition(self.p)
                 AtWall=True
             else:
                self.d=random.randint(0, 360)


R1=Robot(g,1)


# === Problem 3


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, go):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here
    total_steps=0
    AcceptedInput=False
    if go==True:
        AcceptedInput=True
        visualize=True
    if go==False:
        AcceptedInput=True
        visualize=False
    else:
        print("Do you want visualization?")
    while AcceptedInput==False:
        input1=input("Y/N: ")
        print(input1)
        if str(input1)=="N" or str(input1)=="n":
            visualize=False
            AcceptedInput=True
        if str(input1)=="Y" or str(input1)=="y":
            visualize=True
            AcceptedInput=True
        else:
            print("Invalid output")
#    if not 0<=min_coverage<=1.00000000000:
#        raise ValueError
    min_coverage=float(min_coverage)

    trialscollection=[]
    for m in range(num_trials):
        if visualize:
            anim=ps11_visualize.RobotVisualization(num_robots, width, height,)
        testRoom=RectangularRoom(width, height)

        robotList=[]
        for i in range(num_robots):
            robotList.append(robot_type(testRoom, speed))
        percentClean=0.0000000000
        progressList=[]
#        print("First percentClean", percentClean)
        while float(percentClean)<float(min_coverage):
            if visualize:
                anim.update(testRoom, robotList)
            for each in robotList:
                each.updatePositionAndClean()
#            print("cleantiles", testRoom.cleanTiles)
            percentClean=testRoom.getNumCleanedTiles()/testRoom.getNumTiles()
#            print("getNumCleanedTiles", testRoom.getNumCleanedTiles())
#            print("percentClean", percentClean, "MIN_COVERAGE", min_coverage)
            progressList.append(percentClean)
            total_steps+=speed
#            print("Coverage", percentClean)
#        print("are all tiles clean?")
#        for i in range(testRoom.width):
#            for j in range(testRoom.height):
#                print((i,j), testRoom.isTileCleaned(i,j))
        if visualize:
            anim.done()
        trialscollection.append(progressList)
#    averageOfTrials = calcAvgLengthList(trialscollection)

#    print("Total steps", total_steps)
#    print("min_coverage", min_coverage)
#    print("trialscollection", trialscollection)
    return trialscollection

#runSimulation(1, 1, 5, 5, 1, 1, Robot, None)


# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means

def calcAvgLengthList(listOfLists):
    """
    Takes a list of lists and then calculates the average length of the lists
    """
    sumOfLengths = 0
    averageLength = 0
    for eachList in listOfLists:
        sumOfLengths += len(eachList)
    averageLength = sumOfLengths / len(listOfLists)
    # print averageLength
    return averageLength


def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.

    How long does it take a single robot to clean 75% of each of the following types of rooms:
    5x5, 10x10, 15x15, 20x20, 25x25? Output a figure that plots the mean time (on the Y-axis)
    against the area of the room.
    """
    print("""How long does it take a single robot to clean 75% of each of the following types of rooms: 5x5, 10x10, 15x15, 20x20, 25x25? Output a figure that plots the mean time (on the Y-axis) against the area of the room.""")
    square_size = [5,10,15,20,25]
    listOfMeanTimes = []
    for each in square_size:
        trialsCollection = runSimulation(1, 1.0, each, each, 0.75, 25, Robot, False)
        averageOfTrials = calcAvgLengthList(trialsCollection)
        print ("On average, the robot took %i clock ticks to clean 75%% of a %i x %i room." % (int(averageOfTrials), each, each))
        listOfMeanTimes.append(int(averageOfTrials))
        print("listOfMeanTimes", listOfMeanTimes)
    pylab.title("Dependence of cleaning time on room size")
    pylab.xlabel("Room size")
    pylab.ylabel("Time")
    pylab.plot(listOfMeanTimes)
    pylab.show()

#showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here
    numRobots=[1,2,3,4,5,6,7,8,9,10]
    listOfMeanTimes=[]
    for each in numRobots:
        trialsCollection=runSimulation(each, 1.0, 25, 25, 0.75, 25, Robot, False)
        averageOfTrials=calcAvgLengthList(trialsCollection)
        listOfMeanTimes.append(int(averageOfTrials))
    pylab.title("Dependence of cleaning time on no. of robots")
    pylab.xlabel("No. of Robots")
    pylab.ylabel("Time")
    pylab.plot(numRobots, listOfMeanTimes)
    pylab.show()

#showPlot2()

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here
    shapeOfRoom=[[20,20],[25,16],[40,10],[50,8],[80,5],[100,4]]
    w_h=[[20/20],[25/16],[40/10],[50/8],[80/5],[100/4]]
    listOfMeanTimes=[]
    for each in shapeOfRoom:
        trialsCollection=runSimulation(2, 1, each[0], each[1], 0.75, 25, Robot, False)
        averageOfTrials=calcAvgLengthList(trialsCollection)
        print ("On average, the robot took %i clock ticks to clean 75%% of a %i x %i room." % (int(averageOfTrials), each[0], each[1]))
        listOfMeanTimes.append(int(averageOfTrials))
        print("Each[0]", each[0], "Each[1]", each[1], "Each[0]/Each[1]", each[0]/each[1])
    pylab.title("Dependence of cleaning time on shape of room")
    pylab.xlabel("Shape of room")
    pylab.ylabel("Time")
    pylab.plot(w_h, listOfMeanTimes)
    pylab.show()

#showPlot3()

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here
    percentClean = [0.25, 0.5, 0.75, 0.8, 0.9, 1]
    percentCleanList = [[0.25], [0.5], [0.75], [0.8], [0.9], [1]]
    for i in range(1,5+1):
        listOfMeanTimes = []
        for each in percentClean:
            trialsCollection=runSimulation(i, 1.0, 25, 25, each, 25, Robot, False)
            averageOfTrials=calcAvgLengthList(trialsCollection)
            listOfMeanTimes.append(int(averageOfTrials))
        print(percentCleanList, listOfMeanTimes)
        pylab.figure()
        pylab.title("Dependence of cleaning time on min_coverage with " + str(i) + " robots")
        pylab.xlabel("min_coverage")
        pylab.ylabel("Time")
        pylab.plot(percentCleanList, listOfMeanTimes)
    pylab.show()

#showPlot4()

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here
    def updatePositionAndClean(self):
        AtWall=False

        while not AtWall:
             currentPosition=self.getRobotPosition()
             nextPosition=currentPosition.getNewPosition(self.getRobotDirection(), self.speed)
             if self.room.isPositionInRoom(nextPosition):
                 self.p=nextPosition
                 self.room.cleanTileAtPosition(self.p)
                 AtWall=True
                 self.d=random.randint(0,360)
             else:
                self.d=random.randint(0, 360)


#runSimulation(1, 1, 5, 5, 1, 1, RandomWalkRobot, True)

def RshowPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.

    How long does it take a single robot to clean 75% of each of the following types of rooms:
    5x5, 10x10, 15x15, 20x20, 25x25? Output a figure that plots the mean time (on the Y-axis)
    against the area of the room.
    """
    print("""How long does it take a single robot to clean 75% of each of the following types of rooms: 5x5, 10x10, 15x15, 20x20, 25x25? Output a figure that plots the mean time (on the Y-axis) against the area of the room.""")
    square_size = [5,10,15,20,25]
    listOfMeanTimes = []
    for each in square_size:
        trialsCollection = runSimulation(1, 1.0, each, each, 0.75, 25, RandomWalkRobot, False)
        averageOfTrials = calcAvgLengthList(trialsCollection)
        print ("On average, the robot took %i clock ticks to clean 75%% of a %i x %i room." % (int(averageOfTrials), each, each))
        listOfMeanTimes.append(int(averageOfTrials))
        print("listOfMeanTimes", listOfMeanTimes)
    pylab.title("Dependence of cleaning time on room size (regrobot)")
    pylab.xlabel("Room size")
    pylab.ylabel("Time")
    pylab.plot(listOfMeanTimes)
    square_size = [5,10,15,20,25]
    listOfMeanTimes = []
    for each in square_size:
        trialsCollection = runSimulation(1, 1.0, each, each, 0.75, 25, RandomWalkRobot, False)
        averageOfTrials = calcAvgLengthList(trialsCollection)
        print ("On average, the robot took %i clock ticks to clean 75%% of a %i x %i room." % (int(averageOfTrials), each, each))
        listOfMeanTimes.append(int(averageOfTrials))
        print("listOfMeanTimes", listOfMeanTimes)
    pylab.title("Dependence of cleaning time on room size (Robot)")
    pylab.xlabel("Room size")
    pylab.ylabel("Time")
    pylab.plot(listOfMeanTimes)
    pylab.show()


#RshowPlot1()

# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
    percentClean = [0.25, 0.5, 0.75, 0.8, 0.9, 1]
    percentCleanList = [[0.25], [0.5], [0.75], [0.8], [0.9], [1]]
    pylab.figure()
    for i in range(1,5+1):
        listOfMeanTimes = []
        for each in percentClean:
            trialsCollection=runSimulation(i, 1.0, 25, 25, each, 25, Robot, False)
            averageOfTrials=calcAvgLengthList(trialsCollection)
            listOfMeanTimes.append(int(averageOfTrials))
        print(percentCleanList, listOfMeanTimes)
        pylab.title("Dependence of cleaning time on min_coverage with " + str(i) + " robots")
        pylab.xlabel("min_coverage")
        pylab.ylabel("Time")
        pylab.plot(percentCleanList, listOfMeanTimes)
    pylab.figure()
    for i in range(1,5+1):
        listOfMeanTimes = []
        for each in percentClean:
            trialsCollection=runSimulation(i, 1.0, 25, 25, each, 25, RandomWalkRobot, False)
            averageOfTrials=calcAvgLengthList(trialsCollection)
            listOfMeanTimes.append(int(averageOfTrials))
        print(percentCleanList, listOfMeanTimes)
        pylab.title("Dependence of cleaning time on min_coverage with " + str(i) + " RandomWalkRobots")
        pylab.xlabel("min_coverage")
        pylab.ylabel("Time")
        pylab.plot(percentCleanList, listOfMeanTimes)
    pylab.show()

showPlot5()
