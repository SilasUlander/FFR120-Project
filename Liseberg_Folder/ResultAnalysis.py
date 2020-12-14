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


profitDict = {}
fracDict = {}
incomeDict = {}
for dir in dirList:
    if dir[-6:] != 'agents':
        continue
    subDirList = os.listdir(f'Saved_data/{dir}')
    profit = []
    income = []
    fracList = []
    for subDir in subDirList:
        fileList = os.listdir(f'Saved_data/{dir}/{subDir}')
        iAgentData = np.load(f'Saved_data/{dir}/{subDir}/{fileList[0]}', allow_pickle=True).item()
        iAttractionData = np.load(f'Saved_data/{dir}/{subDir}/{fileList[1]}', allow_pickle=True).item()
        iSummary = np.load(f'Saved_data/{dir}/{subDir}/{fileList[2]}', allow_pickle=True).item()
        profit.append(iSummary['profit'])
        fireTime = iSummary['fireTime']

        attractions = ['red', 'brown', 'orange', 'yellow', 'blue']
        tot_income = 0
        for i_attraction in attractions:
            tot_income += iAttractionData[i_attraction].total_income
        income.append(tot_income)

        frac = 0
        n_ave = 0
        for i in iAgentData:
            agent = iAgentData[i]
            try:
                frac += agent.attraction_time / (agent.attraction_time + agent.queue_time)
                n_ave += 1
            except ZeroDivisionError:  # Ignore the ones who just arrived
                pass
        try:
            frac = frac / n_ave
        except ZeroDivisionError:
            frac = 1
        fracList.append(frac)

    profitDict[iSummary['maxAgents']] = np.mean(profit) / fireTime * 1000
    incomeDict[iSummary['maxAgents']] = np.mean(income) / fireTime * 600
    fracDict[iSummary['maxAgents']] = np.mean(fracList) * 7100


sortedProfit = profitDict.items()
profitList = []
for i in sortedProfit:
    subList = [i[0], i[1]]
    profitList.append(subList)

sortedIncome = incomeDict.items()
incomeList = []
for i in sortedIncome:
    subList = [i[0], i[1]]
    incomeList.append(subList)

sortedFrac = fracDict.items()
fracList = []
for i in sortedFrac:
    subList = [i[0], i[1]]
    fracList.append(subList)


profitList = np.array(sorted(profitList))
fracList = np.array(sorted(fracList))
incomeList = np.array(sorted(incomeList))
plt.plot(profitList[:, 0], profitList[:, 1], '-o', label='Profit', zorder=10, color='green')
plt.plot(incomeList[:, 0], incomeList[:, 1], '--o', markersize=4, label='Income', color='orange')
plt.plot(fracList[:, 0], fracList[:, 1], '--o', markersize=4, label='Reputation', color='deepskyblue')
plt.axis([20, 210, 0, 8000])
plt.legend()
plt.xlabel('Maximum number of people in park')
plt.yticks(color='green')
plt.ylabel('Profit (tkr)', color='green')
plt.grid()
plt.show()
