
"""
Function to determine shortest path to next location.

If the next lcoation the robot wants to visit is not a neighbor. This function will be called.

Once the robot finds the gold and has to return back to starting location, this function will also be called.
"""


#0 --> nothing 1 --> breeze, 2 --> stench, 3 --> breeze and a stench, 4 --> glimmer, 8 --> On square with gold
def DFS(matrix, s, e, path):

    if s == e:

        return path

    if s[0] < 0 or s[0] > 3 or s[1] < 0 or s[1] > 3:

        return []

    if not matrix[s[0]][s[1]].isSafe:

        return []


    matrix[s[0]][s[1]].isSafe = False


    up = DFS(matrix, (s[0], s[1] - 1), e, path[:] + [(s[0], s[1] - 1)])
    down = DFS(matrix, (s[0], s[1] + 1), e, path[:] + [(s[0], s[1] + 1)])
    left = DFS(matrix, (s[0] - 1, s[1]), e, path[:] + [(s[0] - 1, s[1])])
    right = DFS(matrix, (s[0] + 1, s[1]), e, path[:] + [(s[0] + 1, s[1])])

    li = [up] + [down] + [left] + [right]
    
    li = list(filter(lambda x: len(x) > 0, li))

    return min(li, key = len) if li else []





    

