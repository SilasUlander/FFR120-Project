import random
import numpy as np


class Agent:
    def __init__(self, index, entrances, mapSize):
        self.index = index
        self.speed = [round(random.uniform(1, 3), 2)]  # speed between 1 and 3 with 2 decimal
        self.mood = [round(random.uniform(1, 3), 1)]  # define a parameter that agent will be satisfied
        self.target = None  # where agent wants to go to
        self.local = 0  # 0: in the pavement, otherwise id of attraction
        self.spawnPosition = random.choice(entrances)
        self.xPos = self.spawnPosition[0]
        self.yPos = self.spawnPosition[1]
        self.move = True  # if true agent moves, if not it means they are in an attraction
        # Map
        self.mapSize = mapSize
        self.mini_map = self.get_minimap()

    def maps(self):
        self.x = [round(random.uniform(0, self.mapSize), 2)]
        self.y = [round(random.uniform(0, self.mapSize), 2)]
        return self.x, self.y

    def entrance(self):
        self.x = [0]
        self.y = [0]
        return self.x, self.y

    def get_mimi_map(self):
        vec = np.array([
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 5, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 6, 0, 0, 5,
            0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
            2, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0,
            0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0,
            0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3,
            0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0])

        mat = vec.reshape((21, 21))

        return mat

    # only meant to run if attraction is not active
    def enter(self, target):
        if self.xPos == target.entrance(1) & self.yPos == target.entrance(2):
            self.local = target.index
            target.people += 1
            # we can add a timer here to measure the time it takes for the attraction to fill in different condition