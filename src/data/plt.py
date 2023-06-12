import random
import time
import numpy
from matplotlib import pyplot as plt

from src.data.data import path


def draw_scatter(positions):
    x_pos = []
    y_pos = []
    for pos in positions:
        if len(pos) != 2:
            raise Exception("position is illegal")
        x_pos.append(pos[0])
        y_pos.append(pos[1])
    plt.scatter(numpy.array(x_pos), numpy.array(y_pos), 5)
    plt.show()


def __random_scatter(num):
    random.seed(time.time())
    x = []
    y = []
    for i in range(0, num):
        x.append(0.5 + random.randint(0, 500) * 1.0 / 1000)
        y.append(0.5 + random.randint(0, 500) * 1.0 / 1000)
    plt.scatter(numpy.array(x), numpy.array(y), 5)
    plt.show()


def __data_scatter():
    x_pos = []
    y_pos = []
    filename = f"{path}/data.txt"
    with open(filename, "r") as f:
        rows = f.readlines()
        for row in rows:
            row = row.replace("\n", "")
            data = row.split(",")
            x_pos.append(float(data[0]))
            y_pos.append(float(data[1]))
    f.close()
    plt.scatter(numpy.array(x_pos), numpy.array(y_pos), 5)
    plt.show()


if __name__ == '__main__':
    __data_scatter()
    __random_scatter(5000)
