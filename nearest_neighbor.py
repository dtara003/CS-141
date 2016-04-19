import sys
import math

class Point :
    # constructor
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val
    # TODO: not used?
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
        # max = (500, 500) and min = (-500, -500) according to generate_test.py
        # maximum distance therefore 1004.98756211
        # set maximum to 10000 instead of 1005 just in case shit goes south
    minimum = 10000
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

def Div_Conq(all):
    # sort array by x coordinates
    # TODO: do we have to sort by y coordinates as well?
    # all.sort(axis=0)
    arr = sorted(all, key=lambda Point: Point.x)
    # check
    print arr
    # for now
    return 0

# --------------------------------------------------------------------------------

list = Read_Points_From_Command_Line_File()
# print list
# Write_to_File("output.txt", list)

# --------------------------------------------------------------------------------

print 'Brute Force - shortest distance: ', Brute_Force(list)
# print 'Divide and Conquer - shortest distance: '

Div_Conq(list)