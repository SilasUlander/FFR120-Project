import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import random
import pylab
from itertools import combinations

a = {1: 'hej',
     2: 'då'}
print(a[1]+a[2])
'''
vec = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 5, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 6, 0, 0, 5,
    0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
    2, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0,
    0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0,
    0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3,
    0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0])

mat = vec.reshape((21, 21))

g = nx.from_numpy_matrix(mat, create_using=nx.Graph())
path = nx.dijkstra_path(g, 0, 5)
print(path[1:])
print(path[:])



#####################################################

def get_target_location(key):
    return target_locations[key]

def add_costumer(agent_id):
    start_pos = random.choice(range(5))
    firstTarget = random.choice(attractions)
    costumers[agentIndex] = Agent(index=agent_id,
                                  entrances=parkEntrances[start_pos],
                                  entrancesStr=parkEntrancesStr[start_pos],
                                 firstTarget=firstTarget,
                                  mapSize=mapSize)


maxAgents = 20

# Agent parameters
probNewCustomer = 0.05  # Probability for agent spawning at each timestep

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

targets_locations

ParkMap = Map(mapSize=mapSize,
              parkEntrances=parkEntrances,
              attractionEntrances=attractionEntrances,
              attractionCorners=attractionCorners)

colors = ['red', 'brown', 'orange', 'yellow', 'blue']
attractions = ['red', 'brown', 'orange', 'yellow', 'blue']
entrance_color = 'black'
ground_color = '#27FF4B'

fig, ax = ParkMap.make_map(colors=colors,
                           entrance_color=entrance_color,
                           ground_color=ground_color)
plt.show()

# Main loop
costumers = {}
customersList = []
agentIndex = 0
for t in range(10000):

    # Let a new customer enter
    if len(costumers) < maxAgents and random.random() < probNewCustomer:
        add_costumer(agentIndex)
        customersList.append(agentIndex)
        costumers.target = random.choice(attractions)

        agentIndex += 1

    for iCostumer in customersList:
        if costumers[iCostumer].move:
            custumers[iCostumer].target
'''
