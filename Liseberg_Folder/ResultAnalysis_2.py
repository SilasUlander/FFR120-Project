import numpy as np
import matplotlib.pyplot as plt
import os
#plt.style.use("dark_background")
maxAgents = 150

queue = np.load(f'Saved_data/queue_vs_time_agents_{maxAgents}.npy', allow_pickle=True)
riding = np.load(f'Saved_data/riding_vs_time_agents_{maxAgents}.npy', allow_pickle=True)

t = range(len(queue[:, 0]))
print(t)

colors = ['red',
          'brown',
          'orange',
          'gold',
          'blue']

colors2 = ['Red',
          'Brown',
          'Orange',
          'Yellow',
          'Blue']
i = 3

fig, ax = plt.subplots(ncols=1, nrows=5, figsize=(7, 9), sharex=True, sharey=True, gridspec_kw={'hspace': 0})

for i in range(5):
    ax[i].plot(t, queue[:, i] + riding[:, i], '--', label='Queue', color=colors[i])
    ax[i].plot(t, riding[:, i], '-', label='Riding', color=colors[i])

    #plt.vlines(x=5000, colors='k', '--', label='Emergency')


    ax[i].axis([0, 5300, 0, 30])
    #ax[i].set_title(colors2[i], fontsize=12)
    #plt.legend()
    if i == 4:
        ax[i].set_xlabel('Time', fontsize=14)

    if i == 0:
        ax[i].set_title(f'Number of agents: {maxAgents}', fontsize=14)

    ax[i].set_ylabel(colors2[i], fontsize=14)
    ax[i].grid()
    ax[i].set_yticks([0, 5, 10, 15, 20, 25])
#fig.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')
plt.tight_layout()
plt.savefig(f'IMAGES/q_vs_r_agents_{maxAgents}.png')
plt.show()
