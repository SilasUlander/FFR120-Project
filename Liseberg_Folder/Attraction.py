import numpy as np

class Attraction:
    def __init__(
            self,
            # index,
            # entrance,  # entrance to attraction
            duration,  # duration of attraction (in ticks?)
            # full,  #  number of people that can go on attraction at the same time
            # excitement,  # excitement of attraction
            # covered,  # does rain prevent it from operating? boolean
            #height,  # height restriction
            # employees,  # number of employees needed to run attraction
            price


    ):
        #self.index = index
        #self.entrance = entrance
        self.duration = duration
        #self.people = 0
        # self.full = full  # is the attraction ready to start
        #self.excitement = excitement
        #self.covered = covered
        # self.height = height
        #self.employees = employees
        #self.active = None
        self.price = price

        # Memory place holder
        self.total_income = 0
        self.queue_list = []
        self.riding_list = []


    def enter_attraction(self, agent):
        id = int(np.copy(agent.index))
        self.queue_list.append(id)


    def sell_ticket(self):
        self.total_income += self.price




'''
    def water(self, wet):
        if self.covered:
            if wet:
                self.active = False

    def start(self, agents):
        for i in agents:
            agents(i).mood(self.excitement)
            agents(i).move = False

    def end(self, agents):
        for i in agents:
            agents(i).move = True

    def run(self):
            self.fill()
'''