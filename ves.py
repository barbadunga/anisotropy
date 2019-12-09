from filter import *
import numpy as np
import matplotlib.pyplot as plt


rho = (10000, 0.1)
h = (3, )

r = np.array(arr_lst(20, 1))
x = np.array(x_lst(r, KF))

k = np.array([[kernel(rho, h, len(rho), xi) for xi in row]for row in x])

rk = rhok(rho, k, G)

plt.plot(r, rk)
plt.yscale('log'); plt.xscale('log')
plt.title('VES')
plt.ylabel('Rho, Om.m')
plt.xlabel('AB/2, m')
plt.grid(True)
plt.show()