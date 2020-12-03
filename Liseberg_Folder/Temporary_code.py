########## CODE FROM AmusementParkOpt ##########

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

########## CODE FROM Agents ##########

'''
    def maps(self):
        self.x = [round(random.uniform(0, self.mapSize), 2)]
        self.y = [round(random.uniform(0, self.mapSize), 2)]
        return self.x, self.y

    def entrance(self):
        self.x = [0]
        self.y = [0]
        return self.x, self.y
'''