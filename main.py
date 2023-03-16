import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def f(x, y) -> float:
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

plt_x = np.arange(min, max, 0.1)
plt_y = np.arange(min, max, 0.1)

xgrid, ygrid = np.meshgrid(plt_x, plt_y)
zgrid = f(xgrid, ygrid)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(xgrid, ygrid, zgrid, color='y', alpha=0.5)  # type: ignore

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')  # type: ignore

plt.show(block=False)

start = datetime.now()

for j in range(10):
    x = rand(min, max)
    y = rand(min, max)

    ax.scatter(x, y, f(x, y), c='red')

    for i in range(10000):
        x -= ex * np.sign(dfdx(x, y, ex))
        y -= ey * np.sign(dfdy(x, y, ey))
        ex = 1 / np.min([i + 1, border])
        ey = 1 / np.min([i + 1, border])

        if i % 1000 == 0:
            ax.scatter(x, y, f(x, y), c='blue')

            fig.canvas.draw()
            fig.canvas.flush_events()

    ax.scatter(x, y, f(x, y), c='blue')

    z = f(x, y)
    if (z < f_min):
        f_min = z
        x_min = x
        y_min = y

print('\n', x_min, y_min, f_min)
print(f'Elapsed {(datetime.now() - start).total_seconds()}s')

plt.show()
