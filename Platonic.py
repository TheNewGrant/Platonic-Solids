# I'm going to be modelling 3D objects for the first time ever.
# So I need to be organized

# Import Turtle so I can draw the shapes.  Import Math for the sin functions
import turtle
import math

# What do I want to do?

"""
I guess my steps should start off with

1: Modelling a point in 3d space  
2: Adding more points into that space and making a line to them
3: Modelling the line correctly (first major test)
4: Bonus, nice: Adding rotation to them (2nd test)
5: Making it so only the necessary number of lines connect to a point
    (A vertex in a cube connect to 3 nearest vertices not all 5)
6: Modelling the cube (only lines) - 3rd test
7: Bonus - Adding faces to them
"""

# Math module sin functions return radians.  Turn into degrees with the degrees() function


# Class to do all these previously mentioned steps
class Model():

    def __init__(self):
        # Initialize turtle and screen classes
        self.screen = turtle.Screen()
        self.dave = turtle.Turtle()
        # Make default parameters of the screen and turtle
        self.SCALE = 250
        self.screen.screensize(self.SCALE * 2, self.SCALE * 2, "white")
        self.dave.color("black", "gray") # Black is the outline, gray is the 
        # filler
        self.dave.shape("circle") # circle shape is best
        self.dave.resizemode("user")
        self.dave.turtlesize(1)
        self.dave.speed(0)
        # create a list to manage all points
        self.pointManage = []


    def testAddPoint(self, x, y, z):
        # Add the cordinants of the points to the manager list
        # create a list to hold compiled points
        compPoints = [x, y, z]
        self.pointManage.append(compPoints.copy()) # .copy() just to be safe
        # print(self.pointManage)
        return self.pointManage


    def drawPoint(self):
        # draw all three coordinant points to this (we are in a 3d space)
        # then omit the z coordinant and draw the point
        # Since each point is only 1 I will multiply each point by
        # 100 for some distance
        point = 0
        for i in self.pointManage:
            x = self.pointManage[point][0]
            y = self.pointManage[point][1]
            self.dave.penup()
            self.dave.setpos(x * 100, y * 100)
            self.dave.stamp()
            # self.dave.setpos(self.SCALE * -2, self.SCALE * -2)
            point += 1
    

    def assignLines(self, numLines):
        # Based off of the assignLines parameter each vertex/point will connect
        # to the nearest numLines of points - numLines = 3, each point will
        # connect to the numLines other points

        # Make sure that if the lenght of pointManage is less than numLInes,
        # then the the points will conect to all of the other points in pointManage
        if numLines > len(self.pointManage):
            numLines = len(self.pointManage)
        
        # Figure out what each point connects to best and draw a line to it
        # ( x and y values to learn angles ), use arc tangent (atan()) to figure out 
        # the angle to aim at (remember to convert to degrees), then use
        # pythagorean theorum to find the length of c.

    
    def makeLine(self, point1Data = [1, 1, 1], point2Data = [1, -1, 1]):
        # Just draw a line to test it out.
        self.dave.penup()

        # Assign x and y changes to variables
        xChange = (point1Data[0] - point2Data[0]) * 100
        yChange = (point1Data[1] - point2Data[1])  * 100
        # If xChange or yChange is 0, then turn it to 1
        if xChange == 0:
            xChange = 1
        if yChange == 0:
            yChange = 1
        # Multiply by negative 1 for accuracy
        xChange *= -1
        yChange *= -1
        print(xChange, yChange)
        # use arc tangent to find the rotation in degrees for the line
        rot = math.degrees(math.atan(yChange/xChange))
        print(rot)
        # Use pythagorean theorum to make a line c between the two points
        c = (xChange ** 2) + (yChange ** 2)
        c = math.sqrt(c)
        print(c)
        # Make the turtle draw there
        self.dave.setpos(point1Data[0], point1Data[1])
        self.dave.seth(0)
        self.dave.left(rot)
        self.dave.pendown()
        self.dave.forward(c)
        return


# --------------------------------Output/Test--------------------------

test = Model()
test.testAddPoint(0, 1, 0)
test.testAddPoint(0, -1, 0)
test.testAddPoint(0, 0, 0)
test.testAddPoint(1, 0.5, 0)
test.testAddPoint(-1, 0.5, 0)
test.testAddPoint(1, -0.5, 0)
test.testAddPoint(-1, -0.5, 0)
# print(test.testAddPoint(1, 1, 1))
test.drawPoint()
test.makeLine()
# print(test.drawPoint)

test.screen.exitonclick()