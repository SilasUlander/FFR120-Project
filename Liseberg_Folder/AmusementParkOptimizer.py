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


def check_if_pos_empty(my_belly,next_pos, id):
    slot_occupied = False
    for i_s in customersInPark:
        if i_s != id:
            p_2 = customers[i_s]
            pos_p2 = np.copy(p_2.pos)
            r_pp = next_pos - pos_p2
            d_between = np.linalg.norm(r_pp)
            if d_between < p_2.bellyRadius + my_belly:
                slot_occupied = True
                break
    return slot_occupied


def update_customer_pos(customer):
    curr_pos = np.copy(customer.pos)
    sub_target_index = customer.path[0]
    sub_target_pos = targets_locations[sub_target_index]

    r_cs = sub_target_pos - curr_pos
    r_cs = r_cs / np.linalg.norm(r_cs)

    next_pos = np.array(np.copy(customer.pos), dtype='float')
    next_pos += customer.speed*r_cs

    slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                       next_pos=next_pos,
                                       id=customer.index)

    angle = np.pi/6
    while angle < (np.pi/2*1.01) and slot_occupied:
        change_vec_r = np.array([np.cos(-2 * angle), np.sin(-2 * angle)])

        right_step = r_cs + change_vec_r
        right_step_vec = right_step / np.linalg.norm(right_step)

        next_pos = customer.speed * right_step_vec

        slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                           next_pos=next_pos,
                                           id=customer.index)
        if slot_occupied:
            break

        change_vec_l = np.array([np.cos(2 * angle), np.sin(2 * angle)])

        left_step = r_cs + change_vec_l
        left_step_vec = left_step / np.linalg.norm(left_step)

        next_pos = customer.speed * left_step_vec

        slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                           next_pos=next_pos,
                                           id=customer.index)

    if not slot_occupied:
        customer.pos = np.copy(next_pos)


def add_customer(agent_id):
    start_pos = random.choice(range(5))
    firstTarget = random.choice(attractions)

    customers[agent_id] = Agent(index=agent_id,
                                entrance=parkEntrances[start_pos],
                                entrancesStr=parkEntrancesStr[start_pos],
                                firstTarget=firstTarget,
                                mapSize=mapSize)
    path = ParkMap.get_path_to_next_pos(customers[agent_id])
    customers[agent_id].path = path
    customersInPark.append(agent_id)
    ParkMap.agentsLocation[agent_id] = customers[agent_id].pos


maxAgents = 20

# Agent parameters
probNewCustomer = 0.05  # Probability for agent spawning at each timestep

# Map parameters
mapSize = 1000

parkEntrances = np.array([[0, 700], [150, 0], [750, 0], [1000, 750], [450, 1000]])
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

targets_locations = [np.array([265, 800]),
                     np.array([450, 1000]),
                     np.array([500, 680]),
                     np.array([310, 400]),
                     np.array([150, 0]),
                     np.array([550, 300]),
                     np.array([750, 0]),
                     np.array([0, 700]),
                     np.array([450, 700]),
                     np.array([750, 510]),
                     np.array([450, 510]),
                     np.array([550, 510]),
                     np.array([265, 700]),
                     np.array([450, 350]),
                     np.array([310, 350]),
                     np.array([150, 350]),
                     np.array([800, 510]),
                     np.array([550, 750]),
                     np.array([1000, 750]),
                     np.array([550, 350]),
                     np.array([750, 350])]

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
customers = {}
customersInPark = []
agentIndex = 0
for t in range(10000):

    # Let a new customer enter
    if len(customersInPark) < maxAgents and random.random() < probNewCustomer:
        add_customer(agentIndex)
        agentIndex += 1

    for iCustomer in customersInPark:
        if customers[iCustomer].move:

            update_customer_pos(customers[iCustomer])
            sub_target_index = customers[iCustomer].path[0]
            sub_target_pos = targets_locations[sub_target_index]

            # Update new pos to map list over all peeeps pos
            if np.linalg.norm(customers[iCustomer].pos - sub_target_pos) < 50:
                print('Göttans')
                customers[iCustomer].path.pop(0)
                if len(customers[iCustomer].path) == 0:
                    customers[iCustomer].move = True  # need to set to true again somehow
                    if customers[iCustomer].satisfied:
                        #find closest exit and leave
                        customersInPark.remove(customers[iCustomer].index)
                    else:
                        customers[iCustomer].location = customers[iCustomer].target
                        while customers[iCustomer].location == customers[iCustomer].target:
                            customers[iCustomer].target = random.choice(attractions)

                        customers[iCustomer].path = ParkMap.get_path_to_next_pos(customers[iCustomer])

