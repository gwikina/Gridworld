from state import state
import numpy as np

class world:
    theWorld = []

    obstacles = [
                    (2,2),
                    (3,2)
                ]
    punish =    [
                    (4,2)
                ]
    start = (0,0)
    goal =  (4,4)

    def __init__(self) -> None:
        # build the world
        self.theWorld = np.empty((5,5),state)
        for i in range(5):
            for j in range(5):
                # check if obstacle 
                if((i,j) in self.obstacles):
                    self.theWorld[i][j] = state(0,False)
                elif((i,j) in self.punish):
                    self.theWorld[i][j] = state(-10,True)
                elif((i,j) == self.goal):
                    self.theWorld[i][j] = state(10,True)
                else:
                    self.theWorld[i][j] = state(0,True)
        self.currentLoc = self.start
        self.acceptedMoves = [ # ORDER HERE MATTERS
                                "up",
                                "right",
                                "down", 
                                "left"
                            ]

    def __confusedRight(self, dir:str) -> str:
        # print("CONFUSED RIGHT")
        idx = self.acceptedMoves.index(dir)
        idx += 1
        if(idx >= len(self.acceptedMoves)):
            idx = 0
        return self.acceptedMoves[idx]

    def __confusedLeft(self, dir:str) -> str:
        # print("CONFUSED LEFT")
        idx = self.acceptedMoves.index(dir)
        idx -= 1
        if(idx < 0):
            idx = len(self.acceptedMoves) - 1
        return self.acceptedMoves[idx]


    def attemptMove(self, dir:str) -> int: #return reward
        # if an unaccaptable move, then throw out the move
        if(dir not in self.acceptedMoves):
            return 0

        newLoc = list(self.currentLoc)
        
        # probabilty for certain environment dynamics
        p = np.random.uniform(0.0,1.0)

        if(0 < p and p <= 0.8): # nothing funny going on here!
            pass 
        elif(0.8 < p and p <= 0.85): # oops! went right
            dir = self.__confusedRight(dir)
        elif(0.85 < p and p <= 0.9): # oops! went left
            dir = self.__confusedLeft(dir)
        elif(p > 0.9 and p <= 1.0): # oops! borked
            return 0

        # Attempt Move
        if(dir == "up"):
            newLoc[0] -= 1
        elif(dir == "down"):
            newLoc[0] += 1
        elif(dir == "left"):
            newLoc[1] -= 1
        elif(dir == "right"):
            newLoc[1] += 1

        # Adjust if attempting to go into bad spot
        if(newLoc[0] < 0 or newLoc[1] < 0):
            newLoc = list(self.currentLoc)
        elif(newLoc[0] > 4 or newLoc[1] > 4):
            newLoc = list(self.currentLoc)
        elif(not self.theWorld[newLoc[0]][newLoc[1]].enterable):
            newLoc = list(self.currentLoc)

        # save move and return reward
        self.currentLoc = tuple(newLoc)
        return self.theWorld[newLoc[0]][newLoc[1]].reward

    def getCurrentLocation(self) -> tuple:
        return self.currentLoc
            

    def display(self) -> None:
        # print world to cmd line
        for i in range(len(self.theWorld)):
            for j in range(len(self.theWorld[i])):
                out = "["
                st = self.theWorld[i][j]
                if((i,j) == self.currentLoc):
                    out += "*"
                elif(not st.enterable):
                    out += "█"
                elif(st.enterable and (st.reward == 0)):
                    out += " "
                elif(st.enterable and (st.reward > 0)):
                    out += "+"
                elif(st.enterable and (st.reward < 0)):
                    out += "-"
                out += "]"
                print(out, end='')
            print('') # force newline