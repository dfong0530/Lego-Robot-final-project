# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:47:30 2021

@author: JV
"""


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
        print(moves)
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
    
            if not(0 <= x < 4) and (0 <= y < 4):
                return False
            elif (not matrix[x][y].isSafe):
                return False

    return True        
def DFS(matrix, sx, sy, ex, ey):   
    solved = False
    queue = [] # queue is actually a list
    recent_path = "" # string
    
    while not solved:
        recent_path = queue.pop(0)
        for i in ["U", "D", "L", "R"]:
            untested_path = recent_path + i
            if legal_move(matrix, untested_path, sx, sy):
                queue.append(untested_path)
        solved = verify(matrix, queue[-1], ex, ey, sx, sy)
        
    return queue[-1]