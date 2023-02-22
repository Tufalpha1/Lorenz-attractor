
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lorenz(t, y, sigma, rho, beta):
    x, y, z = y
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

sigma = 10
rho = 28
beta = 8/3
y0 = [1, 1, 1]
t_span = [0, 100]
sol = solve_ivp(lorenz, t_span, y0, args=(sigma, rho, beta))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
