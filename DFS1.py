
from PointClass import *

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:38:12 2021

"""


# BFS DFS
"""
Function to determine shortest path to next location.

If the next lcoation the robot wants to visit is not a neighbor. This function will be called.

Once the robot finds the gold and has to return back to starting location, this function will also be called.
"""

def process_input(num):
    num_remainder = num
    w, r, g, ag = False, False, False, False # hole, robot, gold, at gold
    while num_remainder > 0: # assumes num is an int
        if num_remainder - 8 >= 0:
            num_remainder -= 8
            ag = True
        elif num_remainder - 4 >= 0:
            num_remainder -= 4
            g = True
        elif num_remainder - 2 >= 0:
            num_remainder -= 2
            r = True
        elif num_remainder >= 0:
            num_remainder -= 1
            w = True
    return (w, r, g, ag)
                
def DFS(matrix, start_x, start_y, ex, ey):
    """
    

    Parameters
    ----------
    matrix : 2D List of Class objects
        This list allows the function to find attributes for specific
        locations, such as num or its safety.
    start_x : int
        DESCRIPTION.
    start_y : int
        DESCRIPTION.
    ex : int
        DESCRIPTION.
    ey : int
        DESCRIPTION.

    Returns
    -------
    direction_ans : list of strings
        DESCRIPTION.

    """

    sx, sy = start_x, start_y
    
    safeSquares = [] # list of tuples of ints that show the safe squares (self.num = 0)
    direction_ans = [] # list of strings: "r" "l" "u" "d"
    visited = [(0, 2)]
    dontWork = [] # list of visited lists that didn't work
    
    for i in range(4): # indiced at (0, 0) for the top left of the matrix
        for j in range(4):
            if matrix[i][j].getNum() == 0:
                temp = (i, j)
                safeSquares.append(temp)


    print(safeSquares, len(safeSquares))
    
    # From your current position, go up, down, left, or right
    
    while True:
        visited = [(0, 2)]
        #print(safeSquares, len(safeSquares))
        while True:
            did_something = False

            #when sx = 0 and sy = 1, (sx, sy) is (0, 1) the top second-to-the-left
            
            # These conditionals ask a) is the proposed move in the grid, b) is the proposed square
            # safe, and c) the robot has not visited the square yet, and d) has this function
            # not tried this way yet (if this move is the last move to an identical path in
            # dontWork, then don't try it again)
            
            # Up

            if ((sx - 1, sy) not in visited):
                visited.append((sx - 1, sy))
            
                print( "(sx - 1 >= 0) and ((sx - 1, sy) in safeSquares) and \
                    and (visited not in dontWork)")
                print( (sx - 1 >= 0), ((sx - 1, sy) in safeSquares), \
                    (visited not in dontWork), "\n\n\n")
                if (sx - 1 >= 0) and ((sx - 1, sy) in safeSquares) and (visited not in dontWork):
                    
                    direction_ans.append("u")
                    sx = sx - 1
                    visited.append((sx, sy))
                    did_something = True

                visited.pop()
            
            #Down

            if ((sx + 1, sy) not in visited):
                visited.append((sx + 1, sy))
    
                print("sx + 1 <= 3) and ((sx + 1, sy) in safeSquares) and \
                     and (visited not in dontWork)")
                print((sx + 1 <= 3), ((sx + 1, sy) in safeSquares), \
                    (visited not in dontWork), "\n\n\n")
                if (sx + 1 <= 3) and ((sx + 1, sy) in safeSquares) and (visited not in dontWork):
                    
                    direction_ans.append("d")
                    sx = sx + 1
                    visited.append((sx, sy))
                    did_something = True
                    
                visited.pop()
            else:
                print("VISITED:", visited)
                
            
            # Left
            
            if ((sx, sy - 1) not in visited):
                
                visited.append((sx, sy - 1))

                if (sy - 1 >= 0) and ((sx, sy - 1) in safeSquares) and (visited not in dontWork):
                        
                    direction_ans.append("l")
                    sy = sy - 1
                    visited.append((sx, sy))
                    did_something = True
               
                visited.pop()
                
                
            # Right
            
            if ((sx, sy + 1) not in visited):
                
                visited.append((sx, sy + 1))

                if (sy + 1 <= 3) and ((sx, sy + 1) in safeSquares) and (visited not in dontWork) :
                        
                    direction_ans.append("r")
                    sy = sy + 1
                    visited.append((sx, sy))
                    did_something = True
                
                visited.pop()

            # No more adjacent safe squares or already visited safe squares
            if not did_something:
                print("Tried", visited, "\ndidn't work")
                dontWork.append(visited)
                direction_ans.clear()
                visited.clear()
                break
            
            if (sx == ex) and (sy == ey):
                return direction_ans
            
    #for i in range(4):
    #   for j in range(4):
    #      if 
    
    
    '''
    Pseudocode


    matrix: List<List<Point>>
    isSafe
    
    sx: int (starting x position)
    sy: int (starting y position)

    ex: int(ending x position)
    ey: int (ending y position)

    Return:

        ["R", "L", "U", "D"]
    '''

def main():
    real = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
    
            ]
    
    manual_matrix = [
        
                [Point(False, True, False, False, 0), Point(False, True, False, False, 1), Point(), Point()],
                [Point(False, True, False, False, 1), Point(False, True, False, False, 1), Point(1), Point()],
                [Point(), Point(), Point(), Point(1)],
                [Point(), Point(1), Point(), Point(1)],
    
            ]
    
    matrix = [[Point() for i in range(4)] for j in range(4)]
    
    print(DFS(manual_matrix, 0, 2, 0, 3))
    print(process_input(9))
    print(process_input(7))
    print(process_input(0))
    
    
    """
    
    []
    queue = 
    col = x row= y
    
    while len(queue) != 0:
        
        x,y = queue.pop()
        
        check up and see if up is == safe squae
        
        check down
        
        checke right
        
        check left
            queue.append((row, col - 1))
            
            
    
    
    
    """


main()