from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
import math
import random
import pylab
import matplotlib.patches as mpatches
from itertools import combinations
from Agents import Agent
from Map import Map
from Attraction import Attraction

matplotlib.use('Qt5Agg')

# Data
parkEntrances = np.array([[0, 700],
                          [150, 0],
                          [750, 0],
                          [1000, 750],
                          [450, 1000]])
parkEntrancesStr = ['W entrance',
                    'NW entrance',
                    'NE entrance',
                    'E entrance',
                    'S entrance']
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
                     np.array([750, 750]),
                     np.array([1000, 750]),
                     np.array([550, 350]),
                     np.array([750, 350])]
colors = ['red',
          'brown',
          'orange',
          'yellow',
          'blue']
attractions = ['red',
               'brown',
               'orange',
               'yellow',
               'blue']
attractions_entrances = {'red': np.array([310.0, 400.0]),
                         'brown': np.array([550.0, 300.0]),
                         'orange': np.array([800.0, 510.0]),
                         'yellow': np.array([500.0, 680.0]),
                         'blue': np.array([265.0, 800.0])}
entrance_color = 'black'
ground_color = '#27FF4B'

######################## Welcome to the latest main// 2020-12-03 #############################


def check_if_pos_empty(my_belly, next_pos, id):
    slot_occupied = False

    # try:
    #     if mapMatrix[int(next_pos[0]), int(next_pos[1])] > 0:
    #         slot_occupied = True
    #         return slot_occupied
    # except:
    #     pass

    for i_s in customersInPark:
        if i_s != id and not customers[i_s].in_queue and not customers[i_s].in_attraction:
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

    next_pos = curr_pos + customer.speed * r_cs

    slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                       next_pos=next_pos,
                                       id=customer.index)

    angle = np.pi / 6
    while angle < (3 / 4 * np.pi * 1.01) and slot_occupied:

        change_vec_r = np.array([np.cos(-2 * angle), np.sin(-2 * angle)]) + np.random.normal(0, .1, 2)
        right_step = r_cs + change_vec_r
        right_step_vec = right_step / np.linalg.norm(right_step)
        next_pos = curr_pos + customer.speed * right_step_vec
        slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                           next_pos=next_pos,
                                           id=customer.index)
        if not slot_occupied:
            break

        change_vec_l = np.array([np.cos(2 * angle), np.sin(2 * angle)]) + np.random.normal(0, .1, 2)
        left_step = r_cs + change_vec_l
        left_step_vec = left_step / np.linalg.norm(left_step)
        next_pos = curr_pos + customer.speed * left_step_vec
        slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                           next_pos=next_pos,
                                           id=customer.index)
        if not slot_occupied:
            break

        angle += np.pi / 6

    if not slot_occupied:
        customer.pos = np.copy(next_pos)


def add_customer(agent_id, time):
    start_pos = random.choice(range(5))
    entrance_occupied = check_if_pos_empty(10, parkEntrances[start_pos], 1e6)
    if entrance_occupied:
        return agent_id
    firstTarget = random.choice(attractions)

    customers[agent_id] = Agent(index=agent_id,
                                entrance=parkEntrances[start_pos],
                                entrancesStr=parkEntrancesStr[start_pos],
                                entranceTime=time,
                                firstTarget=firstTarget,
                                mapSize=mapSize)
    path = ParkMap.get_path_to_next_pos(customers[agent_id])
    customers[agent_id].path = path
    customersInPark.append(agent_id)
    ParkMap.agentsLocation[agent_id] = customers[agent_id].pos
    return agent_id + 1


# Agent parameters
maxAgents = 50
probNewCustomer = 0.5  # Probability for agent spawning at each timestep

# Map parameters
mapSize = 1000
ParkMap = Map(mapSize=mapSize,
              parkEntrances=parkEntrances,
              attractionEntrances=attractionEntrances,
              attractionCorners=attractionCorners)

# Attractions set-up
all_attractions = {}
for i in range(5):
    all_attractions[attractions[i]] = Attraction(duration=100,
                                                 price=25)

# Map plot
fig, ax, mapMatrix = ParkMap.make_map(colors=colors,
                                      entrance_color=entrance_color,
                                      ground_color=ground_color)

ax2 = ax.twinx()
ax2.axes.get_yaxis().set_visible(False)
plt.ion()

# Main loop
customers = {}
customersInPark = []
agentIndex = 0
for t in tqdm(range(10000)):

    for i_attraction in range(5):
        while len(all_attractions[attractions[i_attraction]].riding_list) <= 8 and len(all_attractions[attractions[i_attraction]].queue_list) > 0:
            next_to_enter = all_attractions[attractions[i_attraction]].queue_list.pop(0)
            all_attractions[attractions[i_attraction]].riding_list.append(next_to_enter)
            customers[next_to_enter].enter_attraction_time = t
            customers[next_to_enter].in_queue = False
            customers[next_to_enter].in_attraction = True

        for i_rider in all_attractions[attractions[i_attraction]].riding_list:
            if t - customers[i_rider].enter_attraction_time > all_attractions[attractions[i_attraction]].duration:
                customers[i_rider].move = True
                if np.random.random() < .2:
                    customers[i_rider].location = customers[i_rider].target
                    customers[i_rider].target = random.choice(parkEntrancesStr)
                    customers[i_rider].path = ParkMap.get_path_to_next_pos(customers[i_rider])
                    customers[i_rider].satisfied = True
                all_attractions[attractions[i_attraction]].riding_list.remove(i_rider)
                customers[i_rider].in_attraction = False

                nxt_pos = np.copy(attractions_entrances[customers[i_rider].location])
                while True:
                    is_empty = check_if_pos_empty(my_belly=customers[i_rider].bellyRadius,
                                                  next_pos=nxt_pos,
                                                  id=customers[i_rider].index)
                    if not is_empty:
                        break
                    else:
                        nxt_pos += np.random.uniform(low=-10, high=10, size=2)

                customers[i_rider].pos = np.copy(nxt_pos)
                ParkMap.agentsLocation[customers[i_rider].index] = customers[i_rider].pos

    # Let a new customer enter
    if len(customersInPark) < maxAgents and random.random() < probNewCustomer:
        agentIndex = add_customer(agentIndex, t)

    '''
    if len(ParkMap.agentsLocation.values()) > 0:
        ax2.cla()
        ax2.set_xlim(0, 1000)
        ax2.set_ylim(0, 1000)
        #for iCoord in targets_locations:  # Remove later
        #    ax2.scatter(iCoord[0], 1000 - iCoord[1], c='r')
        # for iCoord in parkEntrances:  # Remove later
        #     ax2.scatter(iCoord[0], 1000 - iCoord[1], c='g')
        all_coords = np.array(list(ParkMap.agentsLocation.values()))
        ax2.scatter(all_coords[:, 0], 1000 - all_coords[:, 1])
        ax2.set_title(fr'$t = {t}$')
        # ax2.legend(str(t))
        queueList = [len(all_attractions['red'].riding_list),
                   len(all_attractions['brown'].riding_list),
                   len(all_attractions['orange'].riding_list),
                   len(all_attractions['yellow'].riding_list),
                   len(all_attractions['blue'].riding_list)]
        tim_patch= mpatches.Patch(alpha=0, label=f'P: {len(customersInPark)}')
        red_patch = mpatches.Patch(color='red', label=f'Q: {queueList[0]}')
        blu_patch = mpatches.Patch(color='blue', label=f'Q: {queueList[4]}')
        yel_patch = mpatches.Patch(color='yellow', label=f'Q: {queueList[3]}')
        bro_patch = mpatches.Patch(color='brown', label=f'Q: {queueList[1]}')
        ora_patch = mpatches.Patch(color='orange', label=f'Q: {queueList[2]}')
        patch_list = [tim_patch, red_patch, blu_patch, yel_patch, bro_patch, ora_patch]
        plt.legend(handles=patch_list, bbox_to_anchor=(1.01, 1), loc='upper right')
        plt.show()
        plt.pause(1e-3)
    '''

    for iCustomer in customersInPark:
        if customers[iCustomer].move:
            update_customer_pos(customers[iCustomer])
            ParkMap.agentsLocation[customers[iCustomer].index] = customers[iCustomer].pos
            sub_target_index = customers[iCustomer].path[0]
            sub_target_pos = targets_locations[sub_target_index]

            # Update new pos to map list over all peeeps pos
            if np.linalg.norm(customers[iCustomer].pos - sub_target_pos) < 20:
                customers[iCustomer].path.pop(0)
                if len(customers[iCustomer].path) == 0:
                    customers[iCustomer].move = False
                    if customers[iCustomer].satisfied:
                        # print(f'EXIT, customer {customers[iCustomer].index}')
                        customersInPark.remove(customers[iCustomer].index)
                        ParkMap.agentsLocation.pop(customers[iCustomer].index)
                        customers[iCustomer].leave(time=t)
                    else:
                        customers[iCustomer].location = customers[iCustomer].target
                        while customers[iCustomer].location == customers[iCustomer].target:
                            customers[iCustomer].target = random.choice(attractions)

                        customers[iCustomer].path = ParkMap.get_path_to_next_pos(customers[iCustomer])

        elif customers[iCustomer].in_queue:
            customers[iCustomer].queue_time += 1

        elif customers[iCustomer].in_attraction:
            # Riding attraction
            aaaaaaa = 123
        else:
            # Enter attraction
            all_attractions[customers[iCustomer].location].enter_attraction(customers[iCustomer])
            all_attractions[customers[iCustomer].location].sell_ticket()
            customers[iCustomer].enter_queue_time = np.copy(t)
            customers[iCustomer].attraction_time += all_attractions[customers[iCustomer].location].duration
            # print(f'Customer {iCustomer}: Time: {customers[iCustomer].attraction_time}')
            customers[iCustomer].in_queue = True

            # Map removal
            ParkMap.agentsLocation.pop(customers[iCustomer].index)

# Stats collection

np.save(f'Saved_data/agent_data_A_{maxAgents}.npy', customers)
np.save(f'Saved_data/attraction_data_A_{maxAgents}.npy', all_attractions)
