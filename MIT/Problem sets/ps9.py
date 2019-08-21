# 6.00 Problem Set 9
#
# Name:
# Collaborators:

from string import *
import copy


class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side
    def __hash__(self):
        return hash(self.side)


class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius
    def __hash__(self):
        return hash(self.radius)

        # Problem 1: Create the Triangle class

#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        self.base=float(base)
        self.height=float(height)
    def area(self):
        return self.base*self.height*0.5
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        return type(other)==Triangle and self.base==other.base and self.height==other.height
    def __hash__(self):
        return hash((self.base, self.height))

T1=Triangle(3.0, 4.0)
#print("Area is", T1.area())
#print(T1)


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.shapes={}
        self.place=None
        self.members=[]
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        self.sh=sh
        In_set=False

        if self.shapes=={}:
            if type(self.sh)==Triangle:
                self.shapes[sh]=(sh.base, sh.height)
            if type(self.sh)==Square:
                self.shapes[sh]=(sh.side)
            if type(self.sh)==Circle:
                self.shapes[sh]=(sh.radius)
            In_set=True


        while In_set==False:
            if not self.shapes=={}:
#                print(self.shapes.values())
#                for i in self.shapes:
#                    print("i", i, "in_set", In_set)
                if type(self.sh)==Triangle:
                    for key in self.shapes:
                        if key=="Triangle":
#                            print("Triangle yes")
                            if (sh.base, sh.height)==self.shapes[key]:
#                                print("Triangle already in set. Breaking")
                                In_set=True
                                return In_set
                        else:
                            pass
#                            print("Key", key)
#                            print("Circle no")
                if type(self.sh)==Square:
                    for key in self.shapes:
                        if key=="Square":
#                            print("yes indeed")
                            if sh.side==self.shapes[key]:
#                                print("Square already in set. Breaking")
                                In_set=True
                                return In_set
                        else:
                            pass
#                            print("key", key)
#                            print("nah bruh")
                if type(self.sh)==Circle:
                    for key in self.shapes:
                        if key=="Circle":
#                            print("Circle yes")
                            if sh.radius==self.shapes[key]:
#                                print("Circle already in set. Breaking")
                                In_set=True
                                return In_set
                        else:
                            pass
#                            print("key", key)
#                            print("Circle no")
#                print("endpoint")
                if type(self.sh)==Triangle:
                    self.shapes[sh]=(sh.base, sh.height)
                    In_set=True
                if type(self.sh)==Square:
                    self.shapes[sh]=(sh.side)
                    In_set=True
                if type(self.sh)==Circle:
                    self.shapes[sh]=(sh.radius)
                    In_set=True
                #return In_set
        return self.shapes

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        self.place=0
        return self
    def __next__(self):
        for i in self.shapes:
            self.members.append(i)
        if self.place >= len(self.shapes):
            raise StopIteration
        else:
            self.place += 1
            return self.members[self.place-1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        for i in self.shapes:
#            print("i is", i)
#            return "oh shit"
            if type(i)==Circle:
                print(Circle(self.shapes[i]))
            if type(i)==Square:
                print(Square(self.shapes[i]))
            if type(i)==Triangle:
                print(Triangle(self.shapes[i][0], self.shapes[i][1]))
        return str()

S1=Square(5.0)
C1=Circle(5.0)
S2=Square(5.0)
C2=Circle(5.0)
T2=Triangle(5.0,2.0)
T12=T1
banana=ShapeSet()
banana.addShape(T1)
#print(banana)
banana.addShape(C2)
banana.addShape(C1)
banana.addShape(C2)
banana.addShape(T12)
banana.addShape(S1)
banana.addShape(S2)
banana.addShape(Triangle(19.0,20.0))
banana.addShape(Square(11))
banana.addShape(Square(20))
banana.addShape(Triangle(80,10))
banana.addShape(Triangle(10,80))
#banana
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    results=()
    All_areas=()
    extras=()
#    print(shapes)
    for i in shapes:
#        print(i)
#        print(i.area())
        areas=(i.area(),)
        All_areas+=areas
#    print(All_areas)
    for a in All_areas:
        if a==max(All_areas):
            results+=(a,)
    final=results+extras
#    print(final)
    return final

#findLargest(banana)

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    testlist=[]
    ShapeSet1=ShapeSet()
    initialized_txt = open(filename, 'r')
    for line in initialized_txt:
        split_line=line.split(",")[0]
        temp_Val1=line.split(",")[1]
        Val1=temp_Val1.strip()
        temp_Val2=line.split(",")[-1]
        Val2=temp_Val2.strip()
#        print(split_line)
#        print(Val1, Val2)
        if split_line=="triangle" or split_line=="Triangle":
            ShapeSet1.addShape(Triangle(Val1,Val2))
#            print("Triangle is true")
#            print("line", line)
#            testlist.append(split_line)
        elif split_line=="circle" or split_line=="Circle":
            ShapeSet1.addShape(Circle(Val1))
        elif split_line=="square" or split_line=="Square":
            ShapeSet1.addShape(Square(Val1))
        else:
            print("Invalid value")
            print(split_line)


#    print(ShapeSet1)
    return ShapeSet1
#        ShapeSet1.addShape(line(value))


SHAPES_FILENAME="shapes.txt"
print(readShapesFromFile(SHAPES_FILENAME))
