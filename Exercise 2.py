from scipy.stats import norm
from csv import writer
import numpy as np
num_points = 10000

def generate_points_vertical(num_points):
    distribution_x = norm(loc=0, scale=100)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0.2, scale=0.05)
    # przy pomocy norm tworzy obiekty reprezentujące\
    # rozkłady prawdopodobieństwa
    # loc=lokalizacja/srednia , scale=odchylenie std.

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)
    # rvs losuje na podstawie ww. obiektów punty o rozmiarze próbki 2000

    points = zip(x, y, z)
    return points


def generate_points_horizontal(num_points):
    distribution_x = norm(loc=0, scale=0.05)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0, scale=100)
    # przy pomocy norm tworzy obiekty reprezentujące\
    # rozkłady prawdopodobieństwa
    # loc=lokalizacja/srednia , scale=odchylenie std.

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)
    # rvs losuje na podstawie ww. obiektów punty o rozmiarze próbki 2000

    points = zip(x, y, z)
    return points

def generate_points_cylinder_2(num_points, radius=30, height=80):
    distribution_x = norm(loc=0, scale=radius)
    distribution_y = norm(loc=0, scale=radius)
    distribution_z = norm(loc=0, scale=height)
    # przy pomocy norm tworzy obiekty reprezentujące\
    # rozkłady prawdopodobieństwa
    # loc=lokalizacja/srednia , scale=odchylenie std.

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)
    # rvs losuje na podstawie ww. obiektów punty o rozmiarze próbki 2000

    points = zip(x, y, z)
    return points

def generate_points_cylinder(num_points):
    t = np.random.uniform(0.0, 5.0*np.pi, 10000)
    r = 3 * np.sqrt(np.random.uniform(0.0, 6.0,10000))
    x = (r * np.cos(t))
    y = r * np.sin(t)
    z = np.random.uniform(0, 30, num_points)
    points = zip(x, y, z)
    return points


if __name__ == '__main__':
    cloud_points_1 = generate_points_vertical(num_points)
    cloud_points_2 = generate_points_horizontal(num_points)
    cloud_points_3 = generate_points_cylinder(num_points)
    cloud_points_4 = generate_points_cylinder_2(num_points)
    with open('LidarData_vertical.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)

        for p in cloud_points_1:
            csvwriter.writerow(p)
    with open('LidarData_horizontal.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)

        for p in cloud_points_2:
            csvwriter.writerow(p)
    with open('LidarData_cylinder.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)

        for p in cloud_points_3:
            csvwriter.writerow(p)

    with open('LidarData_cylinder_2.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)

        for p in cloud_points_4:
            csvwriter.writerow(p)