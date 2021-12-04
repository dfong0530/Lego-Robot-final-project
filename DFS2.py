# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:47:30 2021

@author: JV
"""

from PointClass import *

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

def verify(matrix, moves, ex, ey, sx, sy):
    x = sx
    y = sy
    
    for move in moves: # indiced (0, 0) at top left
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        elif move == "U":
            y -= 1
        elif move == "D":
            y += 1
            
    if (x == ex) and (y == ey):
        #print("SOLVED:", moves)
        return True
    
def legal_move(matrix, testee, sx, sy):
    x = sx
    y = sy
    for move in testee:
            if move == "L":
                x -= 1
    
            elif move == "R":
                x += 1
    
            elif move == "U":
                y -= 1
    
            elif move == "D":
                y += 1
    
            #print(x, y)
            if not(0 <= x < 4) or not(0 <= y < 4):
                return False
            elif (not matrix[x][y].isSafe):
                return False

    return True        
def DFS(matrix, sx, sy, ex, ey):   
    #solved = False
    queue = [] # queue is actually a list
    recent_path = "" # string
    
    while True:
        recent_additions = []
        if len(queue) != 0:
            recent_path = queue.pop(0)
        for i in ["U", "D", "L", "R"]:
            untested_path = recent_path + i
            #print("untested_path ", untested_path)
            if legal_move(matrix, untested_path, sx, sy):
                queue.append(untested_path)
                #print("QUEUE", queue)
                recent_additions.append(untested_path)
        if len(queue) != 0:
            for z in recent_additions:
                if (verify(matrix, z, ex, ey, sx, sy)):
                    return queue[-1]
        #time.sleep(1)
        #print("\n\n\n\n")
    #return list(queue[-1])

'''
def main():
    
    
    manual_matrix = [
        
                [Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, False, False, 0)],
                [Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, True, False, 0), Point(True, False, False, False, 0)],
                [Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, False, False, 0)],
                [Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, False, False, 0), Point(True, False, False, False, 0)],
    
            ]
    
    DFS(manual_matrix, 0, 3, 3, -1)
    
if __name__ == "__main__":
    main()
'''