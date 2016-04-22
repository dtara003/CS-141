"""
.
Author: Dharti Tarapara
Date: 4/22/16
.
I certify that all work shown is my own.
.
"""

import sys
import timeit
import math

class Point :
    # constructor
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val
    # TODO: figure out wtf this is
    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

def Read_Points_From_Command_Line_File():
    # declare an array
    points = []
    # argument count
    number_of_args = len(sys.argv)
    # check if correct number of arguments
    if number_of_args != 2:
        print('ERROR: too many or too few command line args')
        exit(1)
    # open input file
    file = open(sys.argv[1], "r")
    # for every line in the file
    for line in file:
        # assuming this works like the boost's string trim function
        line.strip()
        # make a size-two array with x coordinate and y coordinate
        x_y = line.split(" ")
        # make Point item from x and y coordinates and add to array of points
        points.append(Point(float(x_y[0]), float(x_y[1])))
    # return array of points
    return points

def Write_to_File(filename, s):
    # open output file
    # TODO: what do the 'r' (line 23) and 'w' do? assumption: read and write?
    output = open(filename, 'w')
    # write array of points to file
    output.write(str(s))
    # new line
    output.write('\n')

def Brute_Force(all):
    # give minimum distance a starting value
    minimum = float("inf")
    # go through array replace minimum if smaller value found
    # first two points checked twice but WHATEVER MAN
    for i in range(0, len(all)):
        # go through all possible y coordinates for each
        for j in range(i + 1, len(all)):
            # assign temp current distance value
            temp = math.sqrt(((all[i].y - all[j].y) ** 2) + ((all[i].x - all[j].x) ** 2))
            # compare temp to minimum
            if temp < minimum:
                # check
                # print all[i].x, ', ', all[i].y, '     ', all[j].x, ', ', all[j].y
                # print '\n'
                minimum = temp
    return minimum

def Div(all):
    # cannot determine minimum distance with only one or zero points
    if len(all) < 2:
        return float("inf")
    # if ony two points return distance
    if len(all) == 2:
        return math.sqrt(((all[0].y - all[1].y) ** 2) + ((all[0].x - all[1].x) ** 2))
    # sort array by x coordinates
        # not necessary to do within recursive calls, can be done before call to Div function
    all = sorted(all, key = lambda Point: Point.x)
    # middle point in array
    mid = len(all) / 2
    # make left array everything up to but not including the midpoint
    left = Div(all[:mid])
    # make right array everything from the midpoint to the end
    right = Div(all[mid:])
    # minimum of both left and right minimum distances
    d = min(left, right)
    # lower bound covers everything -d distance from midpoint horizontally
    lower = all[mid].x - d
    # upper bound covers everything d distance from midpoint horizontally
    upper = all[mid].x + d
    # finding start and end of bounded portion of array
    start = 0
    stop = 0
    for i in range(0, len(all)):
        if all[i].x < lower:
            start += 1
        elif all[i].x > upper:
            stop += 1
    bounded = all[start:len(all) - stop]
    # sort bounded array by y coordinates to find 7 closest points in bounded section
    bounded = sorted(bounded, key=lambda Point: Point.y)
    # compare each point to the a maximum of 7 points in front of it for bounded minimum distance
        # modification of brute force
        # outer loop is O(n)
        # inner loop will only execute a maximum of 7 times for every point in array
            # replaces inner O(n) loop with constant runtime and makes loops linear
    for i in range(0, len(bounded)):
        for j in range(1, 8):
            # prevent j from going out of range or from comparing a point with itself or ones before it
            if j < len(bounded):
                if j > i:
                    temp = math.sqrt(((bounded[i].y - bounded[j].y) ** 2) + ((bounded[i].x - bounded[j].x) ** 2))
                    if temp < d:
                        d = temp
    return d

# read in points from file
list = Read_Points_From_Command_Line_File()

# isolate input file name and create output file name
file = sys.argv[1]
file = file[0:len(file)-4]
file = file + "_distance.txt"

# TODO: modify to only output result not twice
start1 = timeit.default_timer()
BF = Brute_Force(list)
stop1 = timeit.default_timer()

start2 = timeit.default_timer()
DC = Div(list)
stop2 = timeit.default_timer()

output = str(BF) + ' ' + str(DC)
# create and write to file
Write_to_File(file, output)

# check timers
print stop1 - start1
print stop2 - start2
