import random
import numpy as np


class Agent:

    def __init__(self, index, entrance, entrancesStr, entranceTime,firstTarget, mapSize, belly):

        # Personal traits
        self.index = index
        self.speed = np.random.uniform(3, 6)  # speed between 1 and 3 with 2 decimal
        self.bellyRadius = belly
        self.mood = [round(random.uniform(1, 3), 1)]  # define a parameter that agent will be satisfied
        self.spawnPosition = entrance  # MIGHT NOT BE NEEDED
        self.satisfied = False

        # Time line
        self.entranceTime = entranceTime
        self.exitTime = np.nan
        self.target = firstTarget  # where agent wants to go to
        self.subTarget = ''
        self.location = entrancesStr  # 0: in the pavement, otherwise id of attraction
        self.pos = entrance
        self.move = True  # if true agent moves, if not it means they are in an attraction
        self.distance_moved = 0
        self.path = []

        self.enter_attraction_time = 0
        self.enter_queue_time = 0
        self.in_attraction = False
        self.attraction_time = 0
        self.in_queue = False
        self.queue_time = 0

        # Map
        self.mapSize = mapSize

    # only meant to run if attraction is not active
    def enter(self, target):
        if self.xPos == target.entrance(1) & self.yPos == target.entrance(2):
            self.location = target.index
            target.people += 1
            # we can add a timer here to measure the time it takes for the attraction to fill in different condition

    def leave(self, time):
        self.exitTime = time
