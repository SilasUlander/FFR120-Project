import random
import numpy as np


class Agent:

    def __init__(self, index, entrances, entrancesStr, mapSize):
        self.index = index
        self.speed = [round(random.uniform(1, 3), 2)]  # speed between 1 and 3 with 2 decimal
        self.mood = [round(random.uniform(1, 3), 1)]  # define a parameter that agent will be satisfied
        self.target = None  # where agent wants to go to
        self.target = None  # where agent wants to go to
        self.spawnPosition = entrances  # MIGHT NOT BE NEEDED
        self.location = entrancesStr  # 0: in the pavement, otherwise id of attraction
        self.xPos = self.spawnPosition[0]
        self.yPos = self.spawnPosition[1]
        self.move = True  # if true agent moves, if not it means they are in an attraction
        self.distance_moved = 0

        # Map
        self.mapSize = mapSize

    # only meant to run if attraction is not active
    def enter(self, target):
        if self.xPos == target.entrance(1) & self.yPos == target.entrance(2):
            self.location = target.index
            target.people += 1
            # we can add a timer here to measure the time it takes for the attraction to fill in different condition

