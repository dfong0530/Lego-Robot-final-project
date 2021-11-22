

"""
4x4 grid - 16 possile slots

1 slot Boss
many slots holes
Every Map solvable

Get Warnings if something dangerous is one of your adjacent neighbors.
Cannot Step out of bounds of the matrix


If you step to a square and you don't recieve warnings then all adjacent squares are safe.


Goal:

    Find Gold
    Avoid Going into pits and robot
    Destroy Robot
    Reuturn to original position



Givens:

    Every time you encounter a warning 
    have to step to a valid square



Prac Siumlation:

    Real Matrix 
    Current Matrix
    Want to make current matrix into real matrix


    Both Matrices store a 2-d list of boolean If it is it is true it is safe. If it is false then it has a danger square.



"""

def PrintMatrix(matrix):

    print("Matrix:")
    print()

    for i in range(len(matrix)):
        
        print("   ",end="")

        for j in range(len(matrix[i])):
            
            print(matrix[i][j], end="  ")

        print()


    
def warning(real, x, y):

    #top
    if y > 0 and not real[y - 1][x]:

        return True

    #bottom
    if y < len(real) - 1 and not real[y + 1][x]:

        return True

    
    #left
    if x > 0 and not real[y][x - 1]:

        return True

    #right
    if x < len(real[y]) - 1 and not real[y][x + 1]:

        return True

    return False


def add_neighbors(matrix, row, col):

    ret = []

    if col > 0 and not matrix[row][col - 1]:

        matrix[row][col - 1] = True
        ret.append((row, col - 1))

    if row < len(matrix) - 1 and not matrix[row + 1][col]:

        matrix[row + 1][col] = True
        ret.append((row + 1, col))

    if col < len(matrix[row]) - 1 and not matrix[row][col + 1]:

        matrix[row][col + 1] = True
        ret.append((row, col + 1))

    if row > 0 and not matrix[row - 1][col]:

        matrix[row - 1][col] = True
        ret.append((row - 1, col))

    return ret




def solve(matrix, real, row, col):

    visit = []
    path = []

    while visit or not path:
    
        w = warning(real, col, row)

        if not w:

            visit += add_neighbors(matrix, row, col)

            path.append((row, col))
            row, col = visit.pop()

        else:

            row, col = path.pop()

        

matrix = [[False, False, False, False],
            [False, False, False, False], 
            [False, False, False,False], 
            [False, False, False, False]]



real = [[False, False, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, False]]


row, col = 3, 0

solve(matrix, real, row, col)


PrintMatrix(matrix)











    


