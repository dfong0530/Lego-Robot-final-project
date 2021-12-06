# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:07:02 2021

@author: JV
"""


"""


Goal is to find Location of Gold. Then move there. finally return location of gold



Notificaiton squares are all safe squares. There could be other safe squares around, danger squares, or unkown squares around.

It needs to use some logic to 100 percent identify squares.


sMatrix will just be a 2-d list of strings of certain squares.


[["s", "h", "g", ""]]
""""


class NotificationSquares(object):
    
    def __init__(row, col, notes):
        
        self.row = row
        self.col = col
        self.notes

        

def numEmpty(matrix, row, col):
    
    tot = 0
    
    if row > 0 and matrix[row - 1][col] == "":
        
        tot += 1
        
    if col < len(matrix[row]) - 1 and matrix[row][col + 1] == "":
        
        tot += 1
        
    if row < len(matrix) - 1 and matrix[row + 1][col] == "":
        
        tot += 1
        
    if col > 0 and matrix[row][col - 1] == "":
        
        tot += 1
        
    return tot
        
    

def findEmpty(matrix, row, col):
    
    
    if row > 0 and matrix[row - 1][col] == "":
        
        return (row - 1, col)
        
    if col < len(matrix[row]) - 1 and matrix[row][col + 1] == "":
        
        return (row, col + 1)
        
    if row < len(matrix) - 1 and matrix[row + 1][col] == "":
        
        return (row + 1, col)
        
    if col > 0 and matrix[row][col - 1] == "":
        
        return (row, col - 1)
    
    return (-1,-1)
        
    return tot
        

def GoldLocation(matrix, row, col):
    
    if numEmpty(matrix,row, col) == 1:
        
        return findEmpty(matrix, row, col)
    
    return (-1,-1)
    

def makeHole(matrix, row, col):
    
    if numEmpty(matrix, row, col) == 1:
        
        loc = findEmpty(matrix, row, col)
        
        matrix[loc[0]][loc[1]] = "h"



def GetSMatrix(matrix):
    
    ret = []
    
    for i in range(len(matrix)):
        
        temp = []
        
        for j in range(len(matrix[i])):
            
            if matrix[i][j].isSafe:
                
                temp.append("s")
                
            else:
                
                temp.append("")
                
        ret.append(temp)
        
    return ret


def note_squares(matrix, noteSquareList):

    
    sMatrix = GetSMatrix(matrix)
    
    i = 0
    
    while i <= 100:
        
        for noteSquare in noteSquareList:
            
            for warning in noteSquare.notes:
                
                if warning == "G":
                    
                    loc = GoldLocation(sMatrix, noteSquare.row, noteSquare.col)
                    
                    if loc != (-1,-1):
                        
                        return loc
                        
                if warning == "H":
                    
                    makeHole(sMatrix, noteSquare.row, noteSquare.col)
                    
            
        i += 1
            
            