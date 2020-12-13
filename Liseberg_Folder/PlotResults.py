import numpy as np
import matplotlib.pyplot as plt


agent_data_load = np.load(f'Saved_data/profit_vs_maxAgents.npy', allow_pickle=True)
maxAgentsList = np.arange(start=10,
                          stop=810,
                          step=10)
plt.plot(maxAgentsList, agent_data_load)
plt.xscale('log')
plt.yscale('log')
plt.show()
