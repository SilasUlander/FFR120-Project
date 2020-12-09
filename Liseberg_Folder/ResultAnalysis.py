import numpy as np
import matplotlib.pyplot as plt

n_Agents = 500

agent_data_load = np.load(f'Saved_data/agent_data_A_{n_Agents}.npy', allow_pickle=True)
attraction_data_load = np.load(f'Saved_data/attraction_data_A_{n_Agents}.npy', allow_pickle=True)
agent_data = agent_data_load.item()
attraction_data = attraction_data_load.item()


tot_income = 0
for i in attraction_data:
    tot_income += attraction_data[i].total_income

frac = 0
n_ave = 0
for i in agent_data:
    agent = agent_data[i]
    try:
        frac += agent.attraction_time/(agent.queue_time + agent.attraction_time)
        n_ave += 1
    except ZeroDivisionError:  # Ignore the once who just arrived
        pass
print(i)
frac = frac/n_ave

profit = tot_income*frac

print(profit)

