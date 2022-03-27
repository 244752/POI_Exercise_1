from sklearn.cluster import KMeans
import numpy as np

num_points = 10000;

divided_clusters = []
cloud_vertical = []
cloud_horizontal = []
cloud_cylinder = []


def divide_into_clusters(num_points, cloud):
    global C1
    global C2
    global C3
    clusterer = KMeans(n_clusters=3)
    X = np.array(cloud)
    y_pred = clusterer.fit_predict(X)
    y_pred_r = [0] * num_points*3
    y_pred_g = [0] * num_points*3
    y_pred_b = [0] * num_points*3

    for p in range(0, num_points):
        if (y_pred[p] == 0):
            y_pred_r[p] = 250
            y_pred_g[p] = 0
            y_pred_b[p] = 0
        elif (y_pred[p] == 1):
            y_pred_r[p] = 0
            y_pred_g[p] = 250
            y_pred_b[p] = 0
        elif (y_pred[p] == 2):
            y_pred_r[p] = 0
            y_pred_g[p] = 0
            y_pred_b[p] = 250

    C1 = y_pred_r
    C2 = y_pred_g
    C3 = y_pred_b

    x, y, z = zip(*cloud)
    color = zip(x, y, z, C1, C2, C3)
    divided_clusters.extend(color)
    return divided_clusters

open("LidarData_vertical.xyz").read()
cloud_vertical = np.genfromtxt("LidarData_vertical.xyz", delimiter=',')
clusters_file_1 = divide_into_clusters(num_points, cloud_vertical)
np.savetxt('LidarData_clusters_vertical.xyz', clusters_file_1, delimiter=',', fmt='%.8f')
open("LidarData_vertical.xyz").close()
divided_clusters = []

open("LidarData_horizontal.xyz").read()
cloud_horizontal = np.genfromtxt("LidarData_horizontal.xyz", delimiter=',')
clusters_file_2 = divide_into_clusters(num_points, cloud_horizontal)
np.savetxt('LidarData_clusters_horizontal.xyz', clusters_file_2, delimiter=',', fmt='%.8f')
open("LidarData_horizontal.xyz").close()
divided_clusters = []

open("LidarData_cylinder.xyz").read()
cloud_cylinder = np.genfromtxt("LidarData_cylinder.xyz", delimiter=',')
clusters_file_3 = divide_into_clusters(num_points, cloud_cylinder)
np.savetxt('LidarData_clusters_cylinder.xyz', clusters_file_3, delimiter=',', fmt='%.8f')
open("LidarData_cylinder.xyz").close()
divided_clusters = []
