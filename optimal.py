from val import ValueIteration

vi = ValueIteration()

# print("initial:")
#vi.display()

i = 0
while not vi.iterate():
    i += 1
    #print("Iteration #", i,":")
    #vi.display()

print("After", i, " iterations...")
vi.display()

policy = vi.getPrettyPolicy()

for i in range(len(policy)):
    for j in range(len(policy[i])):
        print("[",policy[i][j],"]",end='')
        
    print("")