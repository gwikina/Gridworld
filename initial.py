from world import world
from numpy.random import default_rng
import numpy as np
from tqdm import tqdm

def rand2Dir(val:int):
    if(val == 0):
        return "up"
    elif(val == 1):
        return "right"
    elif(val == 2):
        return "down"
    elif(val == 3):
        return "left"

rng = default_rng()
odr = np.empty(10000,dtype=int) # observed discount returns

print("Running 10,000 iterations of a unifromly randomly selected action policy...")
# running 10,000 episodes
for iter in tqdm(range(10000)):
    # create new world
    wrld = world()
    # create empty eposidic reward array
    rewards = np.array([])
    while(True):

        num = rng.integers(0,4,1)[0]
        dir = rand2Dir(num)
        nextReward = wrld.attemptMove(dir)
        rewards = np.append(rewards, nextReward)

        if(nextReward == 10): # We made it to the reward state!
            np.put(odr,iter,rewards.sum())
            break

print("Complete!")
print("Mean: ", odr.mean())
print("Standard Deviation: ", odr.std())
print("Maximum: ", odr.max())
print("Minimuim: ", odr.min())