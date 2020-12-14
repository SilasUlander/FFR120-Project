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
from datetime import datetime
import os

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


######################## Welcome to the latest main// 2020-12-13 #############################


def check_if_pos_empty(my_belly, next_pos, id):
    slot_occupied = False
    switch_id = np.nan
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
                switch_id = i_s
                break
    return slot_occupied, switch_id


def update_customer_pos(customer):
    curr_pos = np.copy(customer.pos)
    sub_target_index = customer.path[0]
    sub_target_pos = targets_locations[sub_target_index]

    r_cs = sub_target_pos - curr_pos
    try:
        r_cs = r_cs / np.linalg.norm(r_cs)
    except:
        print(sub_target_index)
        print(sub_target_pos)
        r_cs = r_cs * 0

    next_pos = curr_pos + customer.speed * r_cs

    slot_occupied, switch_index = check_if_pos_empty(my_belly=customer.bellyRadius,
                                                     next_pos=next_pos,
                                                     id=customer.index)

    angle = -np.pi / 4

    while angle > (-2 * np.pi * 1.01) and slot_occupied:

        change_vec_r = np.array([np.cos(-2 * angle), np.sin(-2 * angle)]) + np.random.normal(0, .1, 2)
        right_step = r_cs + change_vec_r
        right_step_vec = right_step / np.linalg.norm(right_step)
        next_pos = curr_pos + customer.speed * right_step_vec
        slot_occupied, switch_index = check_if_pos_empty(my_belly=customer.bellyRadius,
                                                         next_pos=next_pos,
                                                         id=customer.index)
        if not slot_occupied:
            break
        '''
        change_vec_l = np.array([np.cos(2 * angle), np.sin(2 * angle)]) + np.random.normal(0, .1, 2)
        left_step = r_cs + change_vec_l
        left_step_vec = left_step / np.linalg.norm(left_step)
        next_pos = curr_pos + customer.speed * left_step_vec
        slot_occupied = check_if_pos_empty(my_belly=customer.bellyRadius,
                                           next_pos=next_pos,
                                           id=customer.index)
        if not slot_occupied:
            break
        '''
        angle -= np.pi / 4

    if slot_occupied:
        tmp = np.copy(customers[switch_index].pos)
        customers[switch_index].pos = np.copy(customer.pos)
        customer.pos = tmp

    if not slot_occupied:
        customer.pos = np.copy(next_pos)


def add_customer(agent_id, time, belly_mean):
    start_pos = random.choice(range(5))
    belly_size = max([np.random.normal(loc=belly_mean, scale=2) / 2, 0.001])
    entrance_occupied, _ = check_if_pos_empty(belly_size, parkEntrances[start_pos], np.nan)
    if entrance_occupied:
        return agent_id
    first_target = random.choice(attractions)

    customers[agent_id] = Agent(index=agent_id,
                                entrance=parkEntrances[start_pos],
                                entrancesStr=parkEntrancesStr[start_pos],
                                entranceTime=time,
                                firstTarget=first_target,
                                mapSize=mapSize,
                                belly=belly_size)
    path = ParkMap.get_path_to_next_pos(customers[agent_id])
    customers[agent_id].path = path
    customersInPark.append(agent_id)
    ParkMap.agentsLocation[agent_id] = customers[agent_id].pos
    return agent_id + 1


# Map parameters
mapSize = 1000
ParkMap = Map(mapSize=mapSize,
              parkEntrances=parkEntrances,
              attractionEntrances=attractionEntrances,
              attractionCorners=attractionCorners)
# Map plot
fig, ax, mapMatrix = ParkMap.make_map(colors=colors,
                                      entrance_color=entrance_color,
                                      ground_color=ground_color)

ax2 = ax.twinx()
ax2.axes.get_yaxis().set_visible(False)
plt.ion()

# Set-up #
fireTime = 5000
deadTime = 300
plotFrequency = 20
plot_bool = False

# Agent parameters
belly_mean_size = 10
probNewCustomer = .8
probBecomingSatisfied = .2
maxAgentsList = np.arange(start=50,
                          stop=205,
                          step=5)


profit_vs_maxAgents = np.zeros(len(maxAgentsList))

# Main loop
customers = {}
customersInPark = []
agentIndex = 0
timeForEvacuation = np.nan

for maxAgents in maxAgentsList:
    mainFolder = f'Saved_data/20_days_{maxAgents}_agents'
    os.mkdir(mainFolder)

    for _ in range(20):

        customers = {}
        customersInPark = []
        numDeadCustomers = 0

        agentIndex = 0

        timeForEvacuation = np.nan
        emergency = False

        ParkMap = Map(mapSize=mapSize,
                      parkEntrances=parkEntrances,
                      attractionEntrances=attractionEntrances,
                      attractionCorners=attractionCorners)

        # Attractions set-up
        all_attractions = {}
        for i in range(5):
            all_attractions[attractions[i]] = Attraction(duration=100,
                                                         price=25)

        for t in tqdm(range(10000)):

            if t == fireTime + all_attractions[attractions[0]].duration:
                for i_attraction in range(len(all_attractions)):
                    all_attractions[attractions[i_attraction]].duration = 0

            if t == fireTime:
                emergency = True
                for i_agent in customersInPark:
                    customers[i_agent].speed = customers[i_agent].speed * 2
                    customers[i_agent].Move = True
                    try:
                        customers[i_agent].target = random.choice(parkEntrancesStr)
                        customers[i_agent].path = ParkMap.get_path_to_next_pos(customers[i_agent])
                        customers[i_agent].satisfied = True
                    except IndexError:
                        customers[i_agent].path = [customers[i_agent].location]
                        customers[i_agent].target = [customers[i_agent].location]
                        customers[i_agent].satisfied = True

            if t == fireTime + deadTime:
                print(f'{len(customersInPark)} died')
                numDeadCustomers = customersInPark

            if emergency and len(customersInPark) == 0:
                timeForEvacuation = t - fireTime
                print(f'Time for evacuation: {timeForEvacuation}')
                break

            for i_attraction in range(5):
                while len(all_attractions[attractions[i_attraction]].riding_list) < 8 and len(
                        all_attractions[attractions[i_attraction]].queue_list) > 0:
                    all_attractions[attractions[i_attraction]].sell_ticket()
                    next_to_enter = all_attractions[attractions[i_attraction]].queue_list.pop(0)
                    all_attractions[attractions[i_attraction]].riding_list.append(next_to_enter)
                    customers[next_to_enter].enter_attraction_time = t
                    customers[next_to_enter].in_queue = False
                    customers[next_to_enter].in_attraction = True

                for i_rider in all_attractions[attractions[i_attraction]].riding_list:
                    if t - customers[i_rider].enter_attraction_time > all_attractions[attractions[i_attraction]].duration:
                        customers[i_rider].move = True
                        if np.random.random() < probBecomingSatisfied:
                            customers[i_rider].target = random.choice(parkEntrancesStr)
                            customers[i_rider].path = ParkMap.get_path_to_next_pos(customers[i_rider])
                            customers[i_rider].satisfied = True
                        all_attractions[attractions[i_attraction]].riding_list.remove(i_rider)
                        customers[i_rider].in_attraction = False

                        nxt_pos = np.copy(attractions_entrances[customers[i_rider].location])
                        while True:
                            is_empty, _ = check_if_pos_empty(my_belly=customers[i_rider].bellyRadius,
                                                             next_pos=nxt_pos,
                                                             id=customers[i_rider].index)
                            if not is_empty:
                                break
                            else:
                                nxt_pos += np.random.uniform(low=-10, high=10, size=2)

                        customers[i_rider].pos = np.copy(nxt_pos)
                        ParkMap.agentsLocation[customers[i_rider].index] = customers[i_rider].pos

            # Let a new customer enter
            if len(customersInPark) < maxAgents and random.random() < probNewCustomer and not emergency:
                agentIndex = add_customer(agent_id=agentIndex,
                                          time=t,
                                          belly_mean=belly_mean_size)
            # '''
            if t % plotFrequency == 0 and plot_bool:

                if t % 1 == 0:

                    if len(ParkMap.agentsLocation.values()) > 0:
                        ax2.cla()
                        ax2.set_xlim(0, 1000)
                        ax2.set_ylim(0, 1000)
                        # for iCoord in targets_locations:  # Remove later
                        #    ax2.scatter(iCoord[0], 1000 - iCoord[1], c='r')
                        # for iCoord in parkEntrances:  # Remove later
                        #     ax2.scatter(iCoord[0], 1000 - iCoord[1], c='g')
                        all_coords = np.array(list(ParkMap.agentsLocation.values()))
                        ax2.scatter(all_coords[:, 0], 1000 - all_coords[:, 1])
                        if not emergency:
                            ax2.set_title(fr'$t = {t}$')
                        else:
                            ax2.set_title(fr'FIRE!!! Time until all of the park on fire: {fireTime + deadTime - t}',
                                          color='red')
                        # ax2.legend(str(t))
                        queueList = [len(all_attractions['red'].queue_list),
                                     len(all_attractions['brown'].queue_list),
                                     len(all_attractions['orange'].queue_list),
                                     len(all_attractions['yellow'].queue_list),
                                     len(all_attractions['blue'].queue_list)]
                        ridingList = [len(all_attractions['red'].riding_list),
                                      len(all_attractions['brown'].riding_list),
                                      len(all_attractions['orange'].riding_list),
                                      len(all_attractions['yellow'].riding_list),
                                      len(all_attractions['blue'].riding_list)]
                        patch_list = [
                            mpatches.Patch(alpha=0, label=f'Ppl: {len(customersInPark)}'),
                            mpatches.Patch(color='red', label=f'Queue: {queueList[0]}'),
                            mpatches.Patch(color='blue', label=f'Queue: {queueList[4]}'),
                            mpatches.Patch(color='yellow', label=f'Queue: {queueList[3]}'),
                            mpatches.Patch(color='brown', label=f'Queue: {queueList[1]}'),
                            mpatches.Patch(color='orange', label=f'Queue: {queueList[2]}'),
                            mpatches.Patch(color='red', label=f'Riding: {ridingList[0]}'),
                            mpatches.Patch(color='blue', label=f'Riding: {ridingList[4]}'),
                            mpatches.Patch(color='yellow', label=f'Riding: {ridingList[3]}'),
                            mpatches.Patch(color='brown', label=f'Riding: {ridingList[1]}'),
                            mpatches.Patch(color='orange', label=f'Riding: {ridingList[2]}')]
                        plt.legend(handles=patch_list, bbox_to_anchor=(1.01, 1), loc='upper right')
                        plt.show()
                        plt.pause(1e-3)

            for iCustomer in customersInPark:
                if customers[iCustomer].move:
                    update_customer_pos(customers[iCustomer])
                    ParkMap.agentsLocation[customers[iCustomer].index] = customers[iCustomer].pos
                    sub_target_index = customers[iCustomer].path[0]
                    sub_target_pos = targets_locations[sub_target_index]

                    # Update new pos to map list over all peeeps pos
                    if np.linalg.norm(customers[iCustomer].pos - sub_target_pos) < 20:
                        apa = customers[iCustomer].path.pop(0)
                        customers[iCustomer].location = ParkMap.adjToLoc[apa]
                        if len(customers[iCustomer].path) == 0:
                            customers[iCustomer].move = False
                            if customers[iCustomer].satisfied:
                                # print(f'EXIT, customer {customers[iCustomer].index}')
                                customersInPark.remove(customers[iCustomer].index)
                                ParkMap.agentsLocation.pop(customers[iCustomer].index)
                                customers[iCustomer].leave(time=t)
                            else:
                                # customers[iCustomer].location = customers[iCustomer].target
                                while customers[iCustomer].location == customers[iCustomer].target:
                                    customers[iCustomer].target = random.choice(attractions)

                                customers[iCustomer].path = ParkMap.get_path_to_next_pos(customers[iCustomer])

                elif customers[iCustomer].in_queue:
                    customers[iCustomer].queue_time += 1

                elif customers[iCustomer].in_attraction:
                    # Riding attraction
                    pass
                else:
                    # Enter attraction
                    all_attractions[customers[iCustomer].location].enter_attraction(customers[iCustomer])
                    customers[iCustomer].enter_queue_time = np.copy(t)
                    customers[iCustomer].attraction_time += all_attractions[customers[iCustomer].location].duration
                    # print(f'Customer {iCustomer}: Time: {customers[iCustomer].attraction_time}')
                    customers[iCustomer].in_queue = True

                    # Map removal
                    ParkMap.agentsLocation.pop(customers[iCustomer].index)

        tot_income = 0
        for i_attraction in range(5):
            tot_income += all_attractions[attractions[i_attraction]].total_income

        frac = 0
        n_ave = 0
        for i in customers:
            agent = customers[i]
            try:
                frac += agent.attraction_time / (agent.attraction_time + agent.queue_time)
                n_ave += 1
            except ZeroDivisionError:  # Ignore the once who just arrived
                pass

        try:
            frac = frac / n_ave
        except ZeroDivisionError:
            frac = 1

        print(frac)
        probNewCustomer = frac

        profit = tot_income * frac
        # profit_vs_maxAgents[i_max_agents] = profit

        # Stats collection
        summary = {
            'maxAgents': maxAgents,
            'fireTime': fireTime,
            'deadTime': deadTime,
            'bellyMeanSize': belly_mean_size,
            'probBecomingSatisfied': probBecomingSatisfied,
            'probNewCustomer': probNewCustomer,
            'numDeadCustomers': numDeadCustomers,  # Add default value!!
            'timeForEvacuation': timeForEvacuation,
            'totalTime': t,
            'profit': profit
        }

        mainFolder = f'20_days_{maxAgents}_agents'
        subFolder = str(datetime.now()).replace(' ', '_').replace(':', '-')[:19]
        os.mkdir(f'Saved_data/{mainFolder}/{subFolder}')
        np.save(f'Saved_data/{mainFolder}/{subFolder}/summary', summary)
        np.save(f'Saved_data/{mainFolder}/{subFolder}/agent_dataA{maxAgents}.npy', customers)
        np.save(f'Saved_data/{mainFolder}/{subFolder}/attraction_dataA{maxAgents}.npy', all_attractions)
