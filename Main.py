#!/usr/bin/env python3

from PointClass import Point
from DFS1 import *
from Eric import *


"""
The program workes by taking in an actaul board representing the actual state of the board ie. where the gold,
robot, and holes are.

It then takes in a board with no data and tries to recreate the original board. The only clues the function gets is
if the neighbor has a danger square adjacent to it.

It then uses theese clues to recreate the orginal board.


The function assumes that all squares are danger squares. If the function does not recieve a warning that
there is a hole nearby. The program will set all neighboring squares to safe and then one by one visits safe squares.


0 -> nothing
1 -> Exist a breeze
2 --> stench (Wumpus)
4 --> glitter (gold)
8 --> On Gold square


"""

# def PrintMatrix(matrix):

#     """
#     Displays locations of all holes in the matrix

#     matrix: List<List<Point>>
#     """

#     for i in range(len(matrix)):

#         for j in range(len(matrix[i])):

#             if not matrix[i][j].isSafe:

#                 print(i, j)


"""
Helper Hole functions

"""
    
# def warning(real, x, y, find):

#     """
#     This functions checks for holes, gold, and robots. It takes in the actual matrix and a lcoation(x,y).

#     It also takes in a parameter called find. Find is a string that reprents data about a square.

#     Gold --> "g"
#     hole--> ""
#     robot --> "r"

#     Function searches for find in its neighbors.



#     real: List<List<str>>
#     x: int
#     y: int
#     find: str
#     """

#     #top
#     if y > 0 and real[y - 1][x] == find:

#         return True

#     #bottom
#     if y < len(real) - 1 and real[y + 1][x] == find:

#         return True

    
#     #left
#     if x > 0 and real[y][x - 1] == find:

#         return True

#     #right
#     if x < len(real[y]) - 1 and real[y][x + 1] == find:

#         return True

#     return False



def add_neighbors(matrix, row, col):

    """
    Sets all of the neighbors attributes(isSafe) to True. 

    The algorithm will call this function if it doesn't recieve a notficaiton that there is a hole or a robot nearby.



    Looks North, East South, West. 

    It first checks if it can check north. For example. If the row is 0 it can't check north or elsee there will be an error.

    If looks for squares that are not already safe.
    If then makes the current square safe and adds the coordinate to ret list. 

    ret list will be added to VISIT in the future. 

    matrix: list<list<points>>
    row: int
    col: int 
    """

    ret = []

    if col > 0 and not matrix[row][col - 1].isSafe:

        matrix[row][col - 1].makeSafe()
        ret.append((row, col - 1))

    if row < len(matrix) - 1 and not matrix[row + 1][col].isSafe:

        matrix[row + 1][col].makeSafe()
        ret.append((row + 1, col))

    if col < len(matrix[row]) - 1 and not matrix[row][col + 1].isSafe:

        matrix[row][col + 1].makeSafe()
        ret.append((row, col + 1))

    if row > 0 and not matrix[row - 1][col].isSafe:

        matrix[row - 1][col].makeSafe()
        ret.append((row - 1, col))

    return ret


"""

Helper Gold functions

"""

def find_gold_direc(matrix, row, col):

    if row > 0:
        print("up")
        forward()

        if int(input("Get Data: ")) == 8:

            matrix[row - 1][col].isSafe = True
            return (row - 1, col)

        back()

    if col < len(matrix[row]) - 1:
        print("right")
        right()

        if int(input("Get Data: ")) == 8:
            
            matrix[row][col + 1].isSafe = True
            return (row, col + 1)

        left()

    if row < len(matrix) - 1:
        print("down")
        back()

        if int(input("Get Data: ")) == 8:

            matrix[row + 1][col].isSafe = True
            return (row + 1, col)

        forward()

    if col > 0:
        print("left")
        left()

        if int(input("Get Data")) == 8:

            matrix[row][col - 1].isSafe = True
            return (row, col - 1)

        right()



# def find_gold(real, col, row):

#     """
#     This function finds the gold in the real matrix. I have either recieved a notification that there is gold nearby
#     without recieving a notification that there is a wumpus nearby or have found out that there is a neighbor 
#     with two adjacent sides that have isGold set to True.
#     """

#     if row > 0 and real[row - 1][col] == "g":

#         return (row - 1, col)

#     elif col < 3 and real[row][col + 1] == "g":

#         return (row, col + 1)

#     elif row < 3 and real[row + 1][col] == "g":

#         return (row + 1, col)

#     elif col > 0 and real[row][col - 1] == "g":

#         return (row, col - 1)

#     return (-1,-1)

def check_double_gold(matrix,row, col):

    """
    This function checks if there is a neighbor who has isGold set to True. 

    This function will only be called if I get a gold notification. 

    For example, let's say I get a gold notification. If I find the at one of the 
    neighbors has it's isGold attribute set to True. Then that square is the square with Gold.
    
    """

    if row > 0 and matrix[row - 1][col].isGold:

        return (row - 1, col)

    elif col < 3 and matrix[row][col + 1].isGold:

        return (row, col + 1)

    elif row < 3 and matrix[row + 1][col].isGold:

        return (row + 1, col)

    elif col > 0 and matrix[row][col - 1].isGold:

        return (row, col - 1)

    return (-1, -1)
    

def add_possible_gold(matrix, row, col):

    """
    Sets the attribute isGold of all neighboars to True as long as it isn't a safe square.
    A safe square only has one attribute set to True and that's isSafe.
    
    """

    if row > 0 and not matrix[row - 1][col].isSafe:

        matrix[row - 1][col].isGold = True

    if col < 3 and not matrix[row][col + 1].isSafe:

        matrix[row][col + 1].isGold = True

    if row < 3 and not matrix[row + 1][col].isSafe:

        matrix[row + 1][col].isGold = True

    if col > 0 and not matrix[row][col - 1].isSafe:

        matrix[row][col - 1].isGold = True


"""
Helper Robot functions
"""

# def find_robot_and_make_safe_square(real, row, col):

#     """
#     Very similar to find_gold. This function takes determines exactly where the robot is.
    
#     """

#     if row > 0 and real[row - 1][col] == "r":

#         return [(row - 1, col)]

#     elif col < 3 and real[row][col + 1] == "r":

#         return [(row, col + 1)]

#     elif row < 3 and real[row + 1][col] == "r":

#         return [(row + 1, col)]

#     elif col > 0 and real[row][col - 1] == "r":

#         return [(row, col - 1)]

#     return []

def add_possible_robot(matrix, row, col):

    """
    Takes in a matrix and makes any neighbors that aren't safe have a isRobot attribute set to True.
    """

    if row > 0 and not matrix[row - 1][col].isSafe:

        matrix[row - 1][col].isRobot = True

    if col < 3 and not matrix[row][col + 1].isSafe:

        matrix[row][col + 1].isRobot = True

    if row < 3 and not matrix[row + 1][col].isSafe:

        matrix[row + 1][col].isRobot = True

    if col > 0 and not matrix[row][col - 1].isSafe:

        matrix[row][col - 1].isRobot = True


def check_double_robot(matrix, row, col):

    """
    Checks if there are any neighbors that have the isRobot property set to True.
    """

    if row > 0 and matrix[row - 1][col].isRobot:

        return (row - 1, col)

    elif col < 3 and matrix[row][col + 1].isRobot:

        return (row, col + 1)

    elif row < 3 and matrix[row + 1][col].isRobot:

        return (row + 1, col)
    elif col > 0 and matrix[row][col - 1].isRobot:

        return (row, col - 1)

    return (-1, -1)


def move_robot(direc):

    for d in direc:

        if d == "U":

            forward()

        elif d == "R":

            right()

        elif d == "D":

            back()

        elif d == "L":

            left()

"""
Main Solve Functions

"""

def solve(matrix, row, col):

    """
    This is the main function. It takes in a two 2-d lists.
    The "real" 2-d list is a 2-d lists of one letter strings. This displays the actual state of the board.

    "g" --> gold
    "" --> hole
    "r" --> robot

    The real matrix is a 2-d list. All of the indices are objects from the Point class. All of the indices 
    are intially set to danger squares. When there is no notifications that there is a robot nearby the neighbors
    are set that they are safe.
    """

    visit = []
 
    matrix[3][0].makeSafe()

    while True:

        print(row,col)

        n = int(input("Get Data: "))
        w, r, g, ag = process_input(n)

        if ag:

            return (row, col)
        
        # If we know alll other neighboars
        # IF we get a g twice
        #If g and no warning search all neighbors until gold is found
        
        #All neighboars are safe
        if not w and not g and not r:
           
            visit += add_neighbors(matrix, row, col)

        if not w and not r and g:
            
            return find_gold_direc(matrix, row, col)

        if g:
      
            if check_double_gold(matrix, row, col) != (-1, -1):
         
                final_loc = check_double_gold(matrix, row, col)
                matrix[final_loc[0]][final_loc[1]].isSafe = True
                move_robot(DFS(matrix, col, row, final_loc[1], final_loc[0]))

                return final_loc

            add_possible_gold(matrix, row, col)

        if r:
        
            if check_double_robot(matrix, row, col) != (-1,-1):
                
                # Loc --> [(row, col)]
                #Make the current location safe and add it to visit stack
                loc = check_double_robot(matrix, row, col)
                robot_say("Destroy wumpus at row {0} col {1}".format(loc[0], loc[1]))
                matrix[loc[0]][loc[1]].makeSafe()

                visit.append(loc) 

            else:

                add_possible_robot(matrix, row, col)


        newRow, newCol = visit.pop()
       
        nextPath = DFS(matrix, col, row, newCol, newRow)

        print(nextPath)
        move_robot(nextPath)

        row,col = newRow, newCol



#2-d list of Points
matrix = [[Point() for i in range(4)] for j in range(4)]


#2-d lists of strings
# real = [
#             ["s", "s", "", "g"],
#             ["s", "", "", "s"],
#             ["s", "s", "s", "s"],
#             ["s", "s","s", "s"]

#         ]


#starting locations
row, col = 3, 0

robot_say("Hello I am Wally")



loc = solve(matrix, row, col)




print("----------------------------------------------------")
print()
print(loc)

pathHome = DFS(matrix, loc[1], loc[0], 0, 3)

print(pathHome)

move_robot(pathHome)



