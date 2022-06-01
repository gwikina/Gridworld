from state import state
import numpy as np

class ValueIteration:
    world = []
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
        # build the world!
        self.world = np.empty((5,5),state)
        for i in range(5):
            for j in range(5):
                # check if obstacle 
                if((i,j) in self.obstacles):
                    self.world[i][j] = state(0.0,False)
                elif((i,j) in self.punish):
                    self.world[i][j] = state(-10.0,True)
                elif((i,j) == self.goal):
                    self.world[i][j] = state(10.0,True)
                else:
                    self.world[i][j] = state(0.0,True)
        self.acceptedMoves = [ # ORDER HERE MATTERS
                                "up",
                                "right",
                                "down", 
                                "left"
                            ]

    def __getNextPt(self,startPt:tuple, dir:str) -> tuple:
        if(dir not in self.acceptedMoves):
            return startPt  

        newLoc = list(startPt)
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
            newLoc = list(startPt)
        elif(newLoc[0] > 4 or newLoc[1] > 4):
            newLoc = list(startPt)
        elif(not self.world[newLoc[0]][newLoc[1]].enterable):
            newLoc = list(startPt)
        
        return tuple(newLoc)

    def __getRewardAt(self,pt:tuple) -> int:
        """ Assume pt is good lol"""
        spot = list(pt)
        return self.world[spot[0]][spot[1]].reward

    def __getCorrectRwd(self, startPt:tuple, dir:str) -> int:
        nxtPt = self.__getNextPt(startPt, dir)
        if(nxtPt is startPt):
            return 0.0
        return self.__getRewardAt(nxtPt)

    def __getAccidentRightRwd(self, startPt:tuple, dir:str) -> int:
        idx = self.acceptedMoves.index(dir)
        idx += 1
        if(idx >= len(self.acceptedMoves)):
            idx = 0
        newDir = self.acceptedMoves[idx]
        nxtPt = self.__getNextPt(startPt, newDir)
        if(nxtPt is startPt):
            return 0.0
        return self.__getRewardAt(nxtPt)
    def __getAccidentLeftRwd(self, startPt:tuple, dir:str) -> int:
        idx = self.acceptedMoves.index(dir)
        idx -= 1
        if(idx < 0):
            idx = len(self.acceptedMoves) - 1
        newDir = self.acceptedMoves[idx]
        nxtPt = self.__getNextPt(startPt, newDir)
        if(nxtPt is startPt):
            return 0.0
        return self.__getRewardAt(nxtPt)
        

    def __getPotenialActionReward(self, startPt:tuple, dir:str):
        rwd_correct = self.__getCorrectRwd(startPt, dir)
        rwd_acc_right = self.__getAccidentRightRwd(startPt, dir)
        rwd_acc_left = self.__getAccidentLeftRwd(startPt, dir)
        rwd_broke = 0.0
        return ((0.8 * rwd_correct) + (0.05 * rwd_acc_right) + (0.05 * rwd_acc_left) + (0.1 * rwd_broke))

    def iterate(self) -> bool:
        newWorld = np.copy(self.world)
        for i in range(len(newWorld)):
            for j in range(len(newWorld[i])):
                #if we cannot be in this point skip
                if(not self.world[i][j].enterable):
                    continue
                #if it is a known reward point skip
                if(((i,j) in self.punish) or ((i,j) == self.goal)):
                    continue
                
                up = self.__getPotenialActionReward((i,j),"up") 
                right = self.__getPotenialActionReward((i,j),"right") 
                left = self.__getPotenialActionReward((i,j),"left") 
                down = self.__getPotenialActionReward((i,j),"down")
                
                newWorld[i][j] =  state(-0.04 + max(
                                        up,
                                        right,
                                        left,
                                        down
                                      ), True)
        isEqual = np.array_equal(self.world, newWorld)
        self.world = newWorld
        return isEqual

    def __findBestDir(self, point:tuple)->str:
        pt = list(point)
        up = [pt[0] - 1, pt[1]]
        down = [pt[0] + 1, pt[1]]
        left = [pt[0], pt[1] - 1]
        right = [pt[0], pt[1] + 1]

        if(up[0] < 0):
            upRwd = -100 # crazy negative reward
        else:
            upRwd = self.__getRewardAt(up)

        if(down[0] > 4):
            downRwd = -100 # crazy negative reward
        else:
            downRwd = self.__getRewardAt(down)

        if(left[1] < 0):
            leftRwd = -100 # crazy negative reward
        else:
            leftRwd = self.__getRewardAt(left)

        if(right[1] > 4):
            rightRwd = -100 # crazy negative reward
        else:
            rightRwd = self.__getRewardAt(right)

        rwds = [upRwd, rightRwd, downRwd, leftRwd]
        return self.acceptedMoves[np.argmax(rwds)]       


    def getPrettyPolicy(self):
        policy = np.empty((5,5),str)
        for i in range(5):
            for j in range(5):
                # check if obstacle 
                if((i,j) in self.obstacles):
                    policy[i][j] = "█"
                elif((i,j) in self.punish):
                    policy[i][j] = "-"
                elif((i,j) == self.goal):
                    policy[i][j] = "+"
                else:
                    match self.__findBestDir((i,j)):
                        case "up":
                            policy[i][j] = "↑"
                        case "right":
                            policy[i][j] = "→"
                        case "down":
                            policy[i][j] = "↓"
                        case "left":
                            policy[i][j] = "←"
        return policy

    def getPolicy(self):
        policy = np.empty((5,5),dtype=np.dtype('U100'))
        for i in range(5):
            for j in range(5):
                # check if obstacle 
                if((i,j) in self.obstacles):
                    policy[i][j] = "x"
                elif((i,j) == self.goal):
                    policy[i][j] = "+"
                else:
                    policy[i][j] = self.__findBestDir((i,j))
        return policy
    
    def display(self) -> None:
        # print world to cmd line
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                out = "["
                st = self.world[i][j]
                if(not st.enterable):
                    out += "xxx.xxx"
                elif(st.enterable):
                    out += f'{st.reward:+07.2f}'
                out += "] "
                print(out, end='')
            print('') # force newline