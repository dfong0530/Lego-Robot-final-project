from PointClass import Point


"""
The program workes by taking in an actaul board representing the actual state of the board ie. where the gold,
robot, and holes are.

It then takes in a board with no data and tries to recreate the original board. The only clues the function gets is
if the neighbor has a danger square adjacent to it.

It then uses theese clues to recreate the orginal board.


The function assumes that all squares are danger squares. If the function does not recieve a warning that
there is a hole nearby. The program will set all neighboring squares to safe and then one by one visits safe squares.


"""

def PrintMatrix(matrix):

    """
    Displays locations of all holes in the matrix

    matrix: List<List<Point>>
    """

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if not matrix[i][j].isSafe:

                print(i, j)


    
def warning(real, x, y, find):

    """
    This functions checks for holes, gold, and robots. It takes in the actual matrix and a lcoation(x,y).

    It also takes in a parameter called find. Find is a string that reprents data about a square.

    Gold --> "g"
    hole--> ""
    robot --> "r"

    Function searches for find in its neighbors.



    real: List<List<str>>
    x: int
    y: int
    find: str
    """

    #top
    if y > 0 and real[y - 1][x] == find:

        return True

    #bottom
    if y < len(real) - 1 and real[y + 1][x] == find:

        return True

    
    #left
    if x > 0 and real[y][x - 1] == find:

        return True

    #right
    if x < len(real[y]) - 1 and real[y][x + 1] == find:

        return True

    return False



def add_neighbors(matrix, row, col):

    """
    Sets all of the neighbors attributes(isSafe) to True. 

    The algorithm will call this function if it doesn't recieve a notficaiton that there is a hole or a robot nearby.



    matrix: list<list<points>>
    row: int
    col: int 
    """

    ret = []

    if col > 0 and not matrix[row][col - 1].isSafe:

        matrix[row][col - 1].isSafe = True
        ret.append((row, col - 1))

    if row < len(matrix) - 1 and not matrix[row + 1][col].isSafe:

        matrix[row + 1][col].isSafe = True
        ret.append((row + 1, col))

    if col < len(matrix[row]) - 1 and not matrix[row][col + 1].isSafe:

        matrix[row][col + 1].isSafe = True
        ret.append((row, col + 1))

    if row > 0 and not matrix[row - 1][col].isSafe:

        matrix[row - 1][col].isSafe = True
        ret.append((row - 1, col))

    return ret




def solve(matrix, real, row, col):

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
    path = []

    while visit or not path:
   
        w = warning(real, col, row, "")

        if not w:
           
            visit += add_neighbors(matrix, row, col)

            path.append((row, col))
            row, col = visit.pop()

        else:
   
            row, col = path.pop()

        


#2-d list of Points
matrix = [[Point() for i in range(4)] for j in range(4)]


#2-d lists of strings
real = [
            ["", "", "s", "s"],
            ["s", "s", "s", "s"],
            ["s", "s", "s", "s"],
            ["s", "s","s", ""]

        ]


#starting locations
row, col = 3, 0

solve(matrix, real, row, col)

PrintMatrix(matrix)










    


