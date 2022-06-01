# Gridworld
My grid world project (Swen 711)
<h1> Introduction </h1>
<small> Implementing Grid-world domain that we learned in class. This is done with 3 steps... </small>
<ol>
<li> Have the agent uniformly randomly select actions. Run 10,000 episodes. Report
the mean, standard deviation, maximum, and minimum of the observed
discounted returns. 
</li>
<li> Implement the value iteration algorithm to find the optimal policy. In this case,
the agent will select actions that will provide maximum future discounted
rewards. Report the optimal policy.
</li>
<li>
Run the optimal policy that you found in [2] 10,000 times. Compare the mean,
standard deviation, maximum, and minimum of the observed discounted
returns with [1]
</li>
</ol>

<h1> Environment Dynamics </h1>
<ol>
<li>
p = 0.8
<ul>
  <li>
The correct action is attempted
  </li>
  </ul>
</li>
<li>
p = 0.05
<ul>
  <li>
The agent is confused and moves +90°
  </li>
  </ul>
</li>
<li>
p = 0.05
<ul>
  <li>
The agent is confused and moves-90°
  </li>
  </ul>
</li>
<li>
p = 0.1
<ul>
  <li>
The agent is confused and does not move
  </li>
  </ul>
</li>
</ol>
<h1> Assumptions </h1>
<br />
<small> The agent cannot move out of the world, an attempt to do so will result in no movement </small>

## Part 1
See [initial.py](src/initial.py) for the python code related to part 1. Because of the above Environment Dynamics there is some variablility but a sample statistical analysis of the observed discounted returns is below:
```
Mean:   -26.196
Standard Deviation: 50.85970491459816
Maximum:  10
Minimuim:  -480
```

## Part 2
see [optimal.py](src/optimal.py) for the python code related to Part 2. Below is the world in which the maximum future discounted rewards are displayed. Note that this was found using the Value Iteration method and iterated until the values changes were less than 0.05, which took 14 iterations. Also note that the xxx.xxx spaces represent the obstacles (states that cannot be entered).
```
[+003.74] [+004.24] [+004.79] [+005.40] [+005.96] 
[+004.06] [+004.67] [+005.37] [+006.13] [+006.79] 
[+003.59] [+004.08] [xxx.xxx] [+006.95] [+007.73] 
[+003.16] [+003.56] [xxx.xxx] [+007.82] [+008.79] 
[+002.72] [+002.43] [-010.00] [+008.79] [+010.00] 
```

## Part 3
see [gridworld.py](src/gridworld.py) for the python code related to Part 3. Similarly to Part 1, except using the above policy, it was run 10,000 times and some statistics are shown below.
```
Mean:  10.0
Standard Deviation:  0.0
Maximum:  10.0
Minimuim:  10.0
```
