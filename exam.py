import matplotlib.pyplot as plt
import numpy as np

x = range(101)
xA = 20
xG = 50
rho1 = 10
rho2 = 500
I = 1
dvapi = np.pi * 2
K12 = (rho2 - rho1) / (rho1 + rho2)
rA = [np.abs(xi - xA) for xi in x]
rAi = [np.abs(xi - (2 * xG - xA)) for xi in x]
e0 = [I * rho1 / (2 * np.pi * r) for r in rA]
e = [I * rho1 / dvapi * (1 / rA[i] + K12 / rAi[i]) if x[i] < xG else I * rho1 / dvapi * (1 + K12) / rA[i] for i in range(len(x))]
plt.plot(x, e)
plt.show()