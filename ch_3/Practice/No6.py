import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp

x = np.arange(-4, 4, 0.01)

def gaussian(x, mean, sigma):
    return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mean)**2 / (2*sigma**2))

def gaussian2(x, y, mean, sigma):
    return (1/2*np.pi*sigma**2) * np.exp(-((x-mean)**2 + (y-mean)**2)/(2*sigma**2))

legend = []

plt.plot(x, gaussian(x,0,1))

plt.xlabel('x')
plt.ylabel('density')
plt.legend(legend)
plt.show()

mu = [2,3]
cov = [[2,3],[3,7]]
rv = sp.stats.multivariate_normal(mu, cov)
xx = np.linspace(0,4,120)
yy = np.linspace(1,5,150)

XX, YY = np.meshgrid(xx, yy)
plt.grid(False)
plt.contourf(XX,YY,rv.pdf(np.dstack([XX,YY])))
plt.axis("Equal")
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(XX,YY,rv.pdf(np.dstack([XX,YY])))
plt.show()