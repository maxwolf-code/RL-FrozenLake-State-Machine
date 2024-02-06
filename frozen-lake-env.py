import gymnasium as gym
from time import sleep
import matplotlib.pyplot as plt
#import numpy as np

# env source: 
# https://gymnasium.farama.org/_images/cliff_walking.gif

desc = [
            "FFFFFFFFFF",
            "FFFFFFFFFF",
            "FFFFFFFFFF",
            "SFHHHHHHFG"
            ]

env = gym.make('FrozenLake-v1', desc=desc, is_slippery=True, render_mode="human")

env.reset()
env.render()
sleep(1)

# Where am I? -> in "x" state
print ("Current state", env.s)
# What are my options? -> 4 action
print ("Transitions from current state:", env.P[env.s])

rewards_history = []
observations_history = []
actions_history = []

'''
Actions:

    0: Move left

    1: Move down

    2: Move right

    3: Move up

'''

def execute_action(int_action):
    print ("Action taken:", action)
    next_state, reward, is_terminal, is_truncated, t_prob = env.step(int_action)
    print ("Transition probability:", t_prob)
    print ("Next state:", next_state)
    print ("Reward recieved:", reward)
    print ("Terminal state:", is_terminal)
    env.render()
    #sleep(0.5)
    
    rewards_history.append(reward)
    actions_history.append(int_action)
    observations_history.append(next_state)

    return is_terminal

for exp in range(100):
    print("EXPERIMENT:",exp)
    env.reset()
    is_terminal = False

    rewards_history = []
    observations_history = []
    actions_history = []

    # Test actions ; random selection #
    for _ in range(20):
        if is_terminal:
            break
        action = 3
        is_terminal = execute_action(action)
       
    for _ in range(20):
        if is_terminal:
            break
        action = 2
        is_terminal = execute_action(action)
        
    for _ in range(20):
        if is_terminal:
            break
        action = 1
        is_terminal = execute_action(action)
        
    if rewards_history[-1] == 1.0: 
        plt.plot(rewards_history)
        plt.xlabel('steps')
        plt.ylabel('reward')
        plt.title('Experiment # '+str(exp))
        plt.show()