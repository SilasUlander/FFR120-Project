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



def add_costumer(agent_id):
    start_pos = random.choice(range(5))
    firstTarget = random.choice(attractions)

    costumers[agent_id] = Agent(index=agent_id,
                                entrances=parkEntrances[start_pos],
                                entrancesStr=parkEntrancesStr[start_pos],
                                firstTarget=firstTarget,
                                mapSize=mapSize)
    path = Map.get_path_to_next_pos(costumers[agent_id])
    costumers[agent_id].path = path


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

targets_locations = [np.array(265, 800),
                     np.array(450, 1000),
                     np.array(500, 680),
                     np.array(310, 400),
                     np.array(150, 0),
                     np.array(550, 300),
                     np.array(750, 0),
                     np.array(0, 700),
                     np.array(450, 700),
                     np.array(750, 510),
                     np.array(450, 510),
                     np.array(550, 510),
                     np.array(265, 700),
                     np.array(450, 350),
                     np.array(310, 350),
                     np.array(150, 350),
                     np.array(800, 510),
                     np.array(550, 750),
                     np.array(1000, 750),
                     np.array(550, 350),
                     np.array(750, 350)]

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
customersInPark = []
agentIndex = 0
for t in range(10000):

    # Let a new customer enter
    if len(customersInPark) < maxAgents and random.random() < probNewCustomer:
        add_costumer(agentIndex)
        customersInPark.append(agentIndex)

        agentIndex += 1

    for iCostumer in customersInPark:
        if costumers[iCostumer].move:
            curr_pos = costumers[iCostumer].pos
            sub_target_index = costumers[iCostumer].path[0]
            sub_target_pos = targets_locations[sub_target_index]
            r_cs = sub_target_pos - curr_pos
            r_cs = r_cs/np.linalg.norm(r_cs)
            move_vec = costumers[iCostumer].speed * r_cs
            costumers[iCostumer].pos += move_vec
            # Add new pos to map list over all peeeps pos
            if np.linalg.norm(costumers[iCostumer].pos-sub_target_pos) < 20:
                costumers[iCostumer].path.pop(0)
                if len(costumers[iCostumer].path) == 0:
                    costumers[iCostumer].move = False  # need to set to true again somehow
                    if costumers[iCostumer].satisfied:
                        #find closest exit and leave
                        customersInPark.remove(costumers[iCostumer].index)
                    else:
                        costumers[iCostumer].location = costumers[iCostumer].target
                        while costumers[iCostumer].location == costumers[iCostumer].target:
                            costumers[iCostumer].target = random.choice(attractions)

                        costumers[iCostumer].path = Map.get_path_to_next_pos(costumers[iCostumer])

