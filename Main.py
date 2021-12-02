from Helper.PointClass import Point


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


def find_gold(real, col, row):

    """
    This function finds the gold in the real matrix. I have either recieved a notification that there is gold nearby
    without recieving a notification that there is a wumpus nearby or have found out that there is a neighbor 
    with two adjacent sides that have isGold set to True.
    """

    if row > 0 and real[row - 1][col] == "g":

        return (row - 1, col)

    elif col < 3 and real[row][col + 1] == "g":

        return (row, col + 1)

    elif row < 3 and real[row + 1][col] == "g":

        return (row + 1, col)

    elif col > 0 and real[row][col - 1] == "g":

        return (row, col - 1)

    return (-1,-1)

def check_double_gold(matrix,row, col):

    """
    This function checks if there is a neighbor who has isGold set to True. 

    This function will only be called if I get a gold notification. 

    For example, let's say I get a gold notification. If I find the at one of the 
    neighbors has it's isGold attribute set to True. Then that square is the square with Gold.
    
    """

    if row > 0 and matrix[row - 1][col].isGold:

        return True

    elif col < 3 and matrix[row][col + 1].isGold:

        return True

    elif row < 3 and matrix[row + 1][col].isGold:

        return True

    elif col > 0 and matrix[row][col - 1].isGold:

        return True

    return False
    

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

    if col > 0 and not real[row][col - 1].isSafe:

        matrix[row][col - 1].isGold = True




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
    matrix[3][0].makeSafe()

    while True:
        print(row,col)

        w = warning(real, col, row, "")
        g = warning(real, col, row, "g")
        
        # If we know alll other neighboars
        # IF we get a g twice
        #If g and no warning search all neighbors until gold is found


        #All neighboars are safe
        if not w and not g:
           
            visit += add_neighbors(matrix, row, col)

        elif not w and g:
            
            return find_gold(real, col, row)

        elif g:
      
            if check_double_gold(matrix, row, col):
         
                return find_gold(real, col, row)

            add_possible_gold(matrix, row, col)

            
        row, col = visit.pop()






        


#2-d list of Points
matrix = [[Point() for i in range(4)] for j in range(4)]


#2-d lists of strings
real = [
            ["s", "s", "", "g"],
            ["s", "", "", "s"],
            ["s", "s", "s", "s"],
            ["s", "s","s", "s"]

        ]


#starting locations
row, col = 3, 0

loc = solve(matrix, real, row, col)


print(loc)









    


