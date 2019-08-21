# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:
import ps11_visualize
import math
import random

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
        return Position(round(new_x), round(new_y))
#    def __eq__(self,other):
#        return self.x==other.x and self.y==other.y
    def __hash__(self):
        return hash((self.x, self.y))
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
        intposition=(int(pos.getX()), int(pos.getY()))
        self.cleanTiles[intposition]=self.cleanTiles.get(intposition,0)+1
#        print(cleanTiles)
        return self.cleanTiles

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        self.m, self.n=m, n
#        print("position", Position(self.m, self.n))
        pos=Position(self.m,self.n)
        for i in self.cleanTiles:
#            print("i", i)
#            print("pos", pos)
            if pos==i:
                return True
            if not pos in self.cleanTiles:
#                print("pos: ", pos, "i" )
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
        Clean=0
        for i in self.cleanTiles:
#            print("i",i)
            Clean+=1
        return Clean

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
        self.p=Position(random.randint(0, room.width), random.randint(0, room.height))

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
                  robot_type,):
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
    if not 0<=min_coverage<=1.0:
        raise ValueError

    trialscollection=[]
    for m in range(num_trials):
        if visualize:
            anim=ps11_visualize.RobotVisualization(num_robots, width, height, .02)
        room=RectangularRoom(width, height)

        robotList=[]
        for i in range(num_robots):
            robotList.append(robot_type(room, speed))
        percentClean=0.0000000000
        progressList=[]
#        print("First percentClean", percentClean)
        while percentClean<min_coverage:
            if visualize:
                anim.update(room, robotList)
            for each in robotList:
                each.updatePositionAndClean()
            percentClean=float(room.getNumCleanedTiles())/float(room.getNumTiles())
            print("percentClean", percentClean, "MIN_COVERAGE", min_coverage)
            progressList.append(percentClean)
            total_steps+=speed
#            print("Coverage", percentClean)
        if visualize:
            anim.done()
        trialscollection.append(progressList)
#    averageOfTrials = calcAvgLengthList(trialscollection)

#    print("Total steps", total_steps)
#    print("min_coverage", min_coverage)
#    print("trialscollection", trialscollection)
    return trialscollection

runSimulation(1, 1, 5, 5, 1.000000, 10, Robot)


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


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
