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
        agents.append(Agent(agentIndex, parkEntrances, mapSize))

vec = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 5, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 7, 0, 0, 5,
       0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
       3, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0,
       0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0,
       0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3,
       0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0])

mat = vec.reshape((21, 21))
print(mat)

# agents = []
# for i in range(numAgents):
#     agents.append(Agent(i, map))
#
# positionsX = []
# positionsY = []
# positions = np.zeros(shape=(numAgents + 1, 2))
# distance = np.zeros(shape=(numAgents + 1, numAgents + 1))
# minTwo = np.zeros(shape=(numAgents + 1, 2))
# obviousPoint = []
# redistance = np.zeros(shape=(1, numAgents + 1))
#
# for i in range(numAgents):
#     positionsX.append(round(random.uniform(0, mapSize), 2))
#     positionsY.append(round(random.uniform(0, mapSize), 2))
#
# positionsX.append(0)
# positionsY.append(0)
#
# for j in range(numAgents + 1):
#     positions[j, 0] = positionsX[j]
#     positions[j, 1] = positionsY[j]
#
# for j in range(numAgents + 1):
#     obviousPoint = positions[j]
#
#     for k in range(numAgents + 1):
#         distance[j, k] = (positionsX[k] - obviousPoint[0]) ** 2 + (positionsY[k] - obviousPoint[1]) ** 2
#
# # print(positions,distance)
#
# for i in range(numAgents + 1):
#     reshape = np.argsort(distance[i, :])
#     minTwo[i, 0] = reshape[1]
#     minTwo[i, 1] = reshape[2]
#     # print(reshape)
#
# # print(minTwo, positions)
# # print(positions[1, 0], positions[int(minTwo[1, 0]), 0])
#
# fig = plt.figure(figsize=(16, 8))
# ax1 = fig.add_subplot(111)
# ax1.set_ylim(0 - 10, mapSize + 10)
# ax1.set_xlim(0 - 10, mapSize + 10)
# colors = ['red', 'brown', 'orange', 'yellow', 'blue']  # 5 attractions
# attractions = ['little red', 'little brown', 'little orange', 'little yellow', 'little blue']
# plt.ion()  # make code continue
#
# for p in range(numAgents):
#     ax1.scatter(positions[p][0], positions[p][1], c=colors[p])
#     ax1.plot(positions[p][0], positions[p][1], c=colors[p], label=f'attractions={attractions[p]}')
#
# ax1.plot(0, 0, c='black', label=f'entry/exit')  # entry/exit
# ax1.scatter(0, 0, c='black')
#
# for p in range(numAgents + 1):
#     plt.plot([positions[p, 0], positions[int(minTwo[p, 0]), 0]], [positions[p, 1], positions[int(minTwo[p, 0]), 1]])
#     plt.plot([positions[p, 0], positions[int(minTwo[p, 1]), 0]], [positions[p, 1], positions[int(minTwo[p, 1]), 1]])
#
# fig.canvas.draw()
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('map')
# ax1.legend()
# fig.show()
