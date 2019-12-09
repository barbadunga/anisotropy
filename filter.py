from numpy import exp as exp

KF = 15  # Number of coefficient
KTM = 7  # Number of points on decade
ALFA = 1.005
M = 9  # Offset of main central value between X and r
NC = 10 # Central coefficient
G = (-0.015821, 0.203596, -1.222006, 3.856356, -5.567616, 2.414293, -0.758876, 2.122195, -0.671525, 0.783732,
     -0.290884, 0.169452, -0.031227, 0.003612, 0.004705)  # Filter coefficients

q = 10 ** (1 / KTM)  # Spacing step


class ERModel():
    def __init__(self, rho, height, ns):
        self.rho = rho
        self.h = height
        self.ns = ns

    def __len__(self):
        return self.ns

    def __iter__(self):
        pass


# Calculate array spacing
def arr_lst(NR, r1):
    return [r1 * q ** i for i in range(NR)]


def x_lst(rlst, kf):
    x1 = [r * ALFA / q ** M for r in rlst]
    return [[x * q ** n for n in range(kf)] for x in x1]


def kernel(rho, height, ns, X, i=0):
    if i == ns - 1:
        return 1
    t = rho[i + 1] / rho[i] * kernel(rho, height, ns, X, i + 1)
    f = (1 - t) / (1 + t) * exp(-2 * height[i] / X)

    return (1 - f) / (1 + f)


def rhok(rho, r, g):
    return [rho[0] * sum(row * g) for row in r]