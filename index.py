""" import time """
import numpy as np
""" import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D """

def f(x: float, y: float) -> float:
    return np.sin(x / (np.abs(x - y) + 1)) + np.cos(y / (np.abs(y - x) + 1))

def dfdx(x, y, ex):
    return (f(x + ex, y) - f(x, y)) / ex

def dfdy(x, y, ey):
    return (f(x, y + ey) - f(x, y)) / ey

def rand(min, max):
    return np.random.rand() * (max - min) + min


min = -10
max = 10

ex = 0.1
ey = 0.1
gamma = 0.95

border = 2000

x = 0
y = 0

x_min = 0
y_min = 0
f_min = f(x_min, y_min)

""" plt_x = np.arange(min, max, 0.1)
plt_y = np.arange(min, max, 0.1)

xgrid, ygrid = np.meshgrid(plt_x, plt_y)
zgrid = f(xgrid, ygrid)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(xgrid, ygrid, zgrid, color='y', alpha=0.5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z') """





for j in range(10):

    x = rand(min, max)
    y = rand(min, max)

    """ point = ax.scatter(x, y, f(x, y), c='red') """
    

    for i in range(10000):
        x = x  - ex * np.sign(dfdx(x, y, ex))
        y = y  - ey * np.sign(dfdy(x, y, ey))
        ex = 1 / np.min([i + 1, border])
        ey = 1 / np.min([i + 1, border])

        """ ax.scatter(x, y, f(x, y), c='blue')
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.001) """

    """ time.sleep(1) """

    """ point_end = ax.scatter(x, y, f(x, y), c='blue') """

    z = f(x, y)
    if (z < f_min):
        f_min = z
        x_min = x
        y_min = y

print('\n', x_min, y_min, f_min)

""" plt.ioff()
plt.show() """