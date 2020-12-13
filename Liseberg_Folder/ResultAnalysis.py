import numpy as np
import matplotlib.pyplot as plt
import os

# n_Agents = 500
#
# agent_data_load = np.load(f'Saved_data/agent_data_A_{n_Agents}.npy', allow_pickle=True)
# attraction_data_load = np.load(f'Saved_data/attraction_data_A_{n_Agents}.npy', allow_pickle=True)
# agent_data = agent_data_load.item()
# attraction_data = attraction_data_load.item()
#
#
# tot_income = 0
# for i in attraction_data:
#     tot_income += attraction_data[i].total_income
#
# frac = 0
# n_ave = 0
# for i in agent_data:
#     agent = agent_data[i]
#     try:
#         frac += agent.attraction_time/(agent.exitTime - agent.entranceTime)
#         n_ave += 1
#     except ZeroDivisionError:  # Ignore the once who just arrived
#         pass
# print(i)
# frac = frac/n_ave
#
# profit = tot_income*frac
#
# print(profit)

def get_dir_list(start=None, end=None):
    dir_list = os.listdir('Saved_data')
    if start:
        start_index = dir_list.index(start)
        dir_list = dir_list[start_index:]
    if end:
        end_index = dir_list.index(end)
        dir_list = dir_list[:end_index]
    remove_index = []
    for i, dir in enumerate(dir_list):
        if not os.path.isdir(f'Saved_data/{dir}'):
            remove_index.append(i)
    for i, iRemove in enumerate(remove_index):
        dir_list.pop(iRemove - i)
    return dir_list


dirList = get_dir_list()

for dir in dirList:
    fileList = os.listdir(f'Saved_data/{dir}')
    iAgentData = np.load(f'Saved_data/{dir}/{fileList[0]}', allow_pickle=True).item()
    iAttractionData = np.load(f'Saved_data/{dir}/{fileList[1]}', allow_pickle=True).item()
    iSummary = np.load(f'Saved_data/{dir}/{fileList[2]}', allow_pickle=True).item()

print(iAgentData[0].attraction_time)
print(iAgentData[0].entranceTime)
print(iAgentData[0].exitTime)
frac = iAgentData[0].attraction_time / (iAgentData[0].exitTime - iAgentData[0].entranceTime)
print(frac)
