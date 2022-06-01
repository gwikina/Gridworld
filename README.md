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
