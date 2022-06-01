class state:
    reward = 0
    enterable = False

    def __init__(self, reward:float, isEnterable:bool) -> None:
        self.reward = reward
        self.enterable = isEnterable

    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o, state)):
            if(self.enterable is __o.enterable):
                return (abs(self.reward - __o.reward) < 0.05)
            return False
        return False
    
    def reward(self) -> float:
        return self.reward
    def enterable(self) -> bool:
        return self.enterable