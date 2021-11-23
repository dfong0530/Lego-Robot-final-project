
"""
Point Classes will be stored in the indices in the matrix variable.

It gives data about the indices. If the square isSafe then all other attributes must be set to False.

1. It is possible for a Point to isDangerous and isGold and isRobot. However, if it is safe then it can 
only be safe.


If I get a breeze the state of the point remains as dangerous.

If I get a notification that there is gold nearby then all neigbors will have isGold is set to True.

If I get a notification that ther is a robot nearby then all neigbors will have isRobot set to True.


For the isRobot attribute and the isGold attribute. If I get the notification twice. I can confirm 
where the robot and the gold actually is.

"""

class Point(object):

    def __init__(self, isSafe = False, isDangerous = True, isGold = False, isRobot = False):

        """
        isSafe --> IF this is set to True. Then the square is 100 percent safe and has nothing there.
        isDangerous --> True: There could possibly be a hole.
        isGold --> There could possibly be gold at this Point
        isRobot --> There could possibly be a robot at this Point
        
        """

        self.isSafe = isSafe
        self.isDangerous = isDangerous
        self.isGold = isGold
        self.isRobot = isRobot

    def makeSafe(self):

        """
        Make this point safe and set all attributes to False.
        """

        self.isSafe = True
        self.isDangerous = False
        self.isGold = False
        self.isRobot = False



