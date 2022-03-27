import numpy as np
from scipy.stats import norm
import random
from csv import writer

ERROR = 0.3
EXPECTED_NUMBER_OF_INLIERS = 500
distances_array = []
vectors_array = []
inliers_array = []
inliers_avg = []
cloud = []
i = []

def random_poits_3D(cloud):
    random_pick = random.sample(list(cloud), 1)
    random_p = tuple(random_pick[0])
    return random_p


def plane_3D(cloud):  # wyznaczenie równania płaszczyzny
    a = random_poits_3D(cloud)
    b = random_poits_3D(cloud)
    c = random_poits_3D(cloud)

    #a = random_poits_3D_v2(cloud)
    #b = random_poits_3D_v2(cloud)
    #c = random_poits_3D_v2(cloud)

    vec_va = np.subtract(a, c)
    vec_vb = np.subtract(b, c)

    vec_ua = vec_va / np.linalg.norm(vec_va)
    vec_ub = vec_vb / np.linalg.norm(vec_vb)
    vec_uc = np.cross(vec_ua, vec_ub)  # wyznaczneie wektora Uc wynikiem jest lista z wx, wy, wz
    vec_ucc = []
    vec_ucc.extend(vec_uc)

    d = np.abs(np.sum(np.multiply(vec_uc, c)))  # wyzanczenie odległości d od płaszczyzny

    return vec_ucc, d


def fit_to_plane_points(cloud, vec_ucc, d):  # wyzanczenie odległości poszczególnych punktów
    # od płaszczyzny i określenie jak do niej pasują
    wx = vec_ucc[0]
    wy = vec_ucc[1]
    wz = vec_ucc[2]
    W = [wx, wy, wz]
    distance_p = [(np.abs(wx * point[0] + wy * point[1] + wz * point[2] + d) / np.linalg.norm(vec_ucc)) for point in
                  cloud]
    return distance_p, W


def get_inliers(distance_p):
    inliers = []
    for i in range(0, len(distance_p)):
        if distance_p[i] <= ERROR:
            inliers.append(i)
    return inliers


def average(distances_array):
    return sum(distances_array) / len(distances_array)

def average_inliers(inliers_array):
    x, y, z = zip(*inliers_array)
    x_avg =  sum(np.abs(x)) / len(x)
    y_avg = sum(np.abs(y)) / len(y)
    z_avg = sum(np.abs(z)) / len(z)
    inliers_avg = [x_avg, y_avg, z_avg]
    return inliers_avg


open("LidarData_vertical.xyz").read()
cloud = np.genfromtxt("LidarData_vertical.xyz", delimiter=',')
open("LidarData_vertical.xyz").close()

iter = 0
while True:
    iter += 1
    print(iter)
    vec_ucc, d = plane_3D(cloud)
    distance, W = fit_to_plane_points(cloud, vec_ucc, d)
    i = get_inliers(distance)

    distances_array.extend(distance)
    vectors_array.extend(W)
    if len(i) >= EXPECTED_NUMBER_OF_INLIERS:
        break

print("***************************")
print("No. of iterations: %d" %iter)
print("Vector coordinates: ")
print(W)
distances_avg = average(distances_array)
print("Distances average: %f" %distances_avg)
print("***************************")

inliers = [cloud[inlier] for inlier in i]
np.savetxt('inliers.xyz', inliers, delimiter=',', fmt='%.8f')

open("inliers.xyz").read()
inliers_array = np.genfromtxt("inliers.xyz", delimiter=',')
open("inliers.xyz").close()
print("Inliers average:")
inliers_avg = average_inliers(inliers_array)
print(inliers_avg)

sum_xy = inliers_avg[0]+inliers_avg[1]
sum_yz = inliers_avg[1]+inliers_avg[2]
sum_xz = inliers_avg[0]+inliers_avg[2]

if (distances_avg<=1 and (sum_xy<sum_xz or sum_xy<sum_yz)):
    print("The cloud is a horizontal plane")
elif(distances_avg<=1 and (sum_xy>sum_xz or sum_xy>sum_yz)):
    print("The cloud is a vertical plane")
else:
    print("The cloud is not a plane")
print("***************************")



