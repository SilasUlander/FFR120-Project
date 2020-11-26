import numpy as np
import matplotlib.pylab as plt
import matplotlib


def make_map(corners, entrances, parkEntrances, colors, entrance_color, ground_color):
    fig, ax = plt.subplots()
    map_matrix = np.zeros((1000, 1000))
    for i, iCorners in enumerate(corners):
        for jCorners in iCorners:
            x1 = jCorners[0]
            x2 = jCorners[1]
            y1 = jCorners[2]
            y2 = jCorners[3]
            map_matrix[y1:y2, x1:x2] = i + 1
        entrance_x1 = entrances[i][0]
        entrance_x2 = entrances[i][1]
        entrance_y1 = entrances[i][2]
        entrance_y2 = entrances[i][3]
        map_matrix[entrance_y1:entrance_y2, entrance_x1:entrance_x2] = -1
    for iCoords in parkEntrances:
        entrance_x = iCoords[0]
        entrance_y = iCoords[1]
        map_matrix[max(0, entrance_y-20):entrance_y+20, max(0, entrance_x-20):entrance_x+20] = -1
    map_colors = matplotlib.colors.ListedColormap([entrance_color, ground_color] + colors[:len(corners)])
    ax.imshow(map_matrix, cmap=map_colors, extent=[0, 1000, 0, 1000])
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    return fig, ax



