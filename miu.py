import numpy as np
import matplotlib.pyplot as plt


Zmax = 100
NZ = 500
pi = np.pi

I = 1  # Value of current
rho1 = 5
rho2 = 100
xA = (-11, 0, 0)
K12 = (rho2 - rho1) / (rho2 + rho1)
zl = Zmax / NZ

x = np.linspace(-10, 10, 200)
r = [np.abs(xA[0] - xi) for xi in x]
z = [(2 * i + 1) * zl / 2 for i in range(NZ)]
e0 = [rho1 / (2 * pi * ri) for ri in r]
rz = [np.square(xA[0]) + np.square(zi) for zi in z]
sigma = [K12 * rho1 * (-xA[0]) / (pi * ri) for ri in rz]

e2 = np.zeros_like(e0)
for i in range(len(x)):
    e2i = 0
    for j in range(len(z)):
        e2i += x[i] * zl * sigma[j] / (2 * pi * (x[i] ** 2 + z[j] ** 2))

    e2[i] = e2i

rhok1 = [2 * pi * r[i] * (e0[i] + 2 * e2[i]) for i in range(len(x))]

'''plt.subplot(311)
plt.plot(x, e0)

plt.subplot(312)
plt.plot(x, e2)

plt.subplot(313)'''
plt.plot(x, rhok1)
plt.title('miu')
plt.show()