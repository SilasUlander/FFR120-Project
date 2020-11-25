import numpy as np
import matplotlib.pylab as plt
import matplotlib


def make_map():
    entrance_color = 'black'
    ground_color = '#27FF4B'
    colors = ['red', 'brown', 'orange', 'yellow', 'blue']
    attractions = ['little red', 'little brown', 'little orange', 'little yellow', 'little blue']
    corners = [[[0, 100, 0, 600], [0, 400, 400, 600]],
               [[200, 700, 0, 300]],
               [[800, 1000, 0, 700]],
               [[500, 700, 600, 1000], [600, 1000, 800, 1000]],
               [[0, 400, 800, 1000]]]
    entrances = [[270, 350, 400, 420],
                 [500, 600, 280, 300],
                 [800, 820, 470, 550],
                 [500, 520, 650, 720],
                 [230, 300, 800, 820]]

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
    map_colors = matplotlib.colors.ListedColormap([entrance_color, ground_color] + colors[:len(corners)])
    plt.imshow(map_matrix, cmap=map_colors, extent=[0, 1000, 0, 1000])
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    return plt.gca()



