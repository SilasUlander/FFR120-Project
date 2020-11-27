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

        # Agents location
        self.agentsLocation = []

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
            map_matrix[max(0, entrance_y-20):entrance_y+20, max(0, entrance_x-20):entrance_x+20] = -1
        map_colors = matplotlib.colors.ListedColormap([entrance_color, ground_color] + colors[:len(self.attractionCorners)])
        ax.imshow(map_matrix, cmap=map_colors, extent=[0, 1000, 0, 1000])
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        return fig, ax



