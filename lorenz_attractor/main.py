import collections
import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from matplotlib.animation import FuncAnimation


def lorenz(t, point, parameters):
    x, y, z = point
    s, r, b = parameters
    return [s * (y - x), r * x - y - x * z, x * y - b * z]


class LorenzAttractorIterator:

    def __init__(self, init_state: list[float], parameters: list[float], step: float):
        self.init_state = init_state
        self.parameters = parameters
        self.step = step

        self.ODE = ode(lorenz).set_integrator('dopri5').set_initial_value(init_state, 0).set_f_params(parameters)

    def __next__(self):
        return self.ODE.integrate(self.ODE.t + self.step)


class LorenzAttractor:

    def __init__(self, init_state: list[float], parameters: list[float], step: float):
        self.init_state = init_state
        self.parameters = parameters
        self.step = step

    def __iter__(self):
        return LorenzAttractorIterator(self.init_state, self.parameters, self.step)


attractor1 = LorenzAttractor([1, 2, 3], [10, 28, 8/3], 0.01)
attractor2 = LorenzAttractor([2, 8, 1], [10, 28, 8/3], 0.01)

track1 = []
track2 = []

x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []

i = 0
for state1, state2 in zip(attractor1, attractor2):
    i += 1

    x1.append(state1[0])
    y1.append(state1[1])
    z1.append(state1[2])

    x2.append(state2[0])
    y2.append(state2[1])
    z2.append(state2[2])

    if i == 10000:
        break


# figure
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

plt.sca(axes[0, 0])
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title('x-y projection')

plt.sca(axes[0, 1])
plt.plot(x1, z1)
plt.plot(x2, z2)
plt.title('x-z projection')

plt.sca(axes[1, 0])
plt.plot(z1, y1)
plt.plot(z2, y2)
plt.title('z-y projection')

plt.subplot(2, 2, 4, projection='3d')
plt.title('3d view')
plt.plot(x1, y1, z1)
plt.plot(x2, y2, z2)

plt.tight_layout()
plt.show()
