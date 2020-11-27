import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import random
import pylab
from itertools import combinations
from Agents import Agent
from Map import Map

#####################################################


maxAgents = 20

# Agent parameters
probAgentSpawns = 1  # Probability for agent spawning at each timestep

# Map parameters
mapSize = 1000

parkEntrances = [[0, 700], [150, 0], [750, 0], [1000, 750], [450, 1000]]
parkEntrancesStr = ['W entrance', 'NW entrance', 'NE entrance', 'E entrance', 'S entrance']


attractionCorners = [[[0, 100, 0, 600], [0, 400, 400, 600]],
                     [[200, 700, 0, 300]],
                     [[800, 1000, 0, 700]],
                     [[500, 700, 600, 1000], [600, 1000, 800, 1000]],
                     [[0, 400, 800, 1000]]]
attractionEntrances = [[280, 350, 400, 420],
                       [500, 600, 280, 300],
                       [800, 820, 470, 550],
                       [500, 520, 650, 720],
                       [230, 300, 800, 820]]

ParkMap = Map(mapSize=mapSize,
              parkEntrances=parkEntrances,
              attractionEntrances=attractionEntrances,
              attractionCorners=attractionCorners)

colors = ['red', 'brown', 'orange', 'yellow', 'blue']
attractions = ['little red', 'little brown', 'little orange', 'little yellow', 'little blue']
entrance_color = 'black'
ground_color = '#27FF4B'

fig, ax = ParkMap.make_map(colors=colors,
                           entrance_color=entrance_color,
                           ground_color=ground_color)
plt.show()

# Main loop
agents = []
agentIndex = 0
for t in range(100):
    if len(agents) < maxAgents and random.random() < probAgentSpawns:
        # Spawn agent
        agentIndex += 1

        start_pos = random.choice(range(5))
        agents.append(Agent(index=agentIndex,
                            entrances=parkEntrances[start_pos],
                            entrancesStr=parkEntrancesStr[start_pos],
                            mapSize=mapSize))



