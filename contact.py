import numpy as np
import matplotlib.pyplot as plt


I = 1  # Current value [A]
rho2 = 100  # Apparent resistivity of first layer [Om*m]
rho1 = 5  # Apparent resistivity of first layer [Om*m]
xA = (-101, 0, 0)

x = range(-100, 101, 1)
k = I * rho1 / (2 * np.pi)
K12 = (rho2 - rho1) / (rho1 + rho2)  # Coefficient of current reflection
rA = [np.sqrt(np.square(xi - xA[0])) for xi in x]
rAi = [np.sqrt(np.square(xi + xA[0])) for xi in x]

e = []
for i in range(len(x)):
    if i < int(len(x) / 2):
        e.append(k * (1 / np.square(rA[i]) + K12 / np.square(rAi[i])))
    else:
        e.append(k * (1 + K12) / np.square(rA[i]))

rhok = []
for i in range(len(x)):
    if i < int(len(x) / 2) and x[i] < xA[0]:
        ri = rho1 * (1 + K12 * np.square(rA[i]) / np.square(rAi[i]))
    elif xA[0] < x[i] and i < int(len(x) / 2):
        ri = rho1 * (1 - K12 * np.square(rA[i]) / np.square(rAi[i]))
    else:
        ri = 2 * rho1 * rho2 / (rho1 + rho2)

    rhok.append(ri)


plt.subplot()
plt.plot(x, rhok)
plt.title('analit')
plt.show()