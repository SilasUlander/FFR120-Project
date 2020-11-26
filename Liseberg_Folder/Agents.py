import random


class Agent:
    def __init__(self, index, entrances):
        self.index = index
        self.speed = [round(random.uniform(1, 3), 2)]  # speed between 1 and 3 with 2 decimal
        self.mood = [round(random.uniform(1, 3), 1)]  # define a parameter that agent will be satisfied
        self.target = None  # where agent wants to go to
        self.spawnPosition = random.choice(entrances)
        self.xPos = self.spawnPosition[0]
        self.yPos = self.spawnPosition[1]

    def maps(self):
        self.x = [round(random.uniform(0, self.mapSize), 2)]
        self.y = [round(random.uniform(0, self.mapSize), 2)]
        return self.x, self.y

    def entrance(self):
        self.x = [0]
        self.y = [0]
        return self.x, self.y
