from world import world
import numpy as np
from tqdm import tqdm
from val import ValueIteration

vi = ValueIteration()

# print("initial:")
#vi.display()

i = 0
while not vi.iterate():
    i += 1

policy = vi.getPolicy()
odr = np.empty(10000,dtype=float) # observed discount returns

print("Running 10,000 iterations of a Value Iterated policy...")
# running 10,000 episodes
for iter in tqdm(range(10000)):
    # create new world
    wrld = world()
    # create empty eposidic reward array
    rewards = np.array([])
    while(True):

        currLoc = wrld.getCurrentLocation()
        dir = policy[currLoc[0], currLoc[1]]
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