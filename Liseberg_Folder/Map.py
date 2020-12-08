import networkx as nx
import numpy as np
import matplotlib.pylab as plt
import matplotlib


class Map:
    def __init__(self, mapSize, parkEntrances, attractionEntrances, attractionCorners):

        # Map properties
        self.mapSize = mapSize
        self.attractionEntrances = attractionEntrances
        self.parkEntrances = parkEntrances
        self.attractionCorners = attractionCorners

        self.locToAdj, self.G = self.create_connections()

        # Agents location
        self.agentsLocation = {}

    def make_map(self, colors, entrance_color, ground_color):
        fig, ax = plt.subplots()
        map_matrix = np.zeros((1000, 1000))
        for i, iCorners in enumerate(self.attractionCorners):
            for jCorners in iCorners:
                x1 = jCorners[0]
                x2 = jCorners[1]
                y1 = jCorners[2]
                y2 = jCorners[3]
                map_matrix[y1:y2, x1:x2] = i + 1
            entrance_x1 = self.attractionEntrances[i][0]
            entrance_x2 = self.attractionEntrances[i][1]
            entrance_y1 = self.attractionEntrances[i][2]
            entrance_y2 = self.attractionEntrances[i][3]
            map_matrix[entrance_y1:entrance_y2, entrance_x1:entrance_x2] = -1
        for iCoords in self.parkEntrances:
            entrance_x = iCoords[0]
            entrance_y = iCoords[1]
            map_matrix[max(0, entrance_y - 20):entrance_y + 20, max(0, entrance_x - 20):entrance_x + 20] = -1
        map_colors = matplotlib.colors.ListedColormap(
            [entrance_color, ground_color] + colors[:len(self.attractionCorners)])
        ax.imshow(map_matrix, cmap=map_colors, extent=[0, 1000, 0, 1000])
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)
        ax.set_aspect('auto')
        return fig, ax, map_matrix

    def get_path_to_next_pos(self, agent):

        current_pos = agent.location
        target_pos = agent.target

        path = nx.dijkstra_path(self.G, self.locToAdj[current_pos], self.locToAdj[target_pos])
        path_len = nx.dijkstra_path_length(self.G, self.locToAdj[current_pos], self.locToAdj[target_pos])

        return path[1:]

    def create_connections(self):
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
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 8, 0, 0, 2, 6, 0, 6, 5,
            0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 6, 8,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
            2, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 5, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0,
            0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0,
            0, 0, 0, 0, 0, 2, 0, 0, 0, 6, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3,
            0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 8, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0])


        mat = vec.reshape((21, 21))

        g = nx.from_numpy_matrix(mat, create_using=nx.Graph())

        adj = {'NW entrance': 4,
               'NE entrance': 6,
               'W entrance': 7,
               'E entrance': 18,
               'S entrance': 1,
               'brown': 5,
               'red': 3,
               'orange': 16,
               'yellow': 2,
               'blue': 0}

        return adj, g
