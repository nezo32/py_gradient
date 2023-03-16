import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def f(x, y) -> float:
    return (x**2 + 5) * (y**2 + 12)


def dfdx(x, y, ex):
    return (f(x + ex, y) - f(x, y)) / ex


def dfdy(x, y, ey):
    return (f(x, y + ey) - f(x, y)) / ey


def rand(min, max):
    return np.random.rand() * (max - min) + min


iter = 100000

min = -50
max = 50

ex = 0.1
ey = 0.1

border = 5000

x = 0
y = 0

x_min = 0
y_min = 0
f_min = f(x_min, y_min)

plt_x = np.arange(-100, 100, 0.1)
plt_y = np.arange(-100, 100, 0.1)

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
    x = rand(min, max + 1)
    y = rand(min, max + 1)

    ax.scatter(x, y, f(x, y), c='red')

    for i in range(iter):
        x -= ex * np.sign(dfdx(x, y, ex))
        y -= ey * np.sign(dfdy(x, y, ey))
        ex = 1 / np.min([i + 1, border])
        ey = 1 / np.min([i + 1, border])

        if i % (iter // 5) == 0:
            ax.scatter(x, y, f(x, y), c='blue')

            fig.canvas.draw()
            fig.canvas.flush_events()
            

    ax.scatter(x, y, f(x, y), c='green')

    z = f(x, y)
    if (z < f_min):
        f_min = z
        x_min = x
        y_min = y

print('\n', x_min, y_min, f_min)
print(f'Elapsed {(datetime.now() - start).total_seconds()}s')

plt.show()
