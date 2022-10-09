import numpy as np
import matplotlib.pyplot as plt
import math
v0 = 1000
def ctg(x):
    return 1 / math.tan(x)

plt.title('Зависимость |ψ| = f(v/v0) ')

plt.minorticks_on()
plt.grid(which='major',linewidth = 1,color = 'black',linestyle = '--')
plt.grid(which='minor',color = 'k',linestyle = ':')

plt.xlabel('v/v0', color='gray')
plt.ylabel('|ψ|[рад/π]',color='gray')
ny = np.array([0.41,0.4,0.37,0.2,0,0.125,0.185,0.4,0.43])
nx= np.array([800,850,900,950,1000,1020,1040,1140,1200])
nx = nx/v0

nyy = np.array([0.425,0.42,0.4125,0.38,0.3,0.18,0+0.07,0.115,0.155,0.25,0.36,0.425,0.45,0.47])
nyy = nyy - 0.05
nxx= np.array([760,780,800,850,900,950,1000,1020,1040,1100,1140,1200,1250,1300])
nxx = nxx/v0

zz = np.polyfit(nxx[0:8], nyy[0:8], 5)
zz2 = np.polyfit(nxx[7:145], nyy[7:15], 3)
xxp = np.linspace(0.75, 1, 100)
xxp2 = np.linspace(1,1.3,100)
pp = np.poly1d(zz)
pp2 = np.poly1d(zz2)


z = np.polyfit(nx[0:5], ny[0:5], 3)
z2 = np.polyfit(nx[4:10], ny[4:10], 3)
xp = np.linspace(0.8, 1, 100)
xp2 = np.linspace(1,1.2,100)
p = np.poly1d(z)
p2 = np.poly1d(z2)
_ = plt.plot( xp, p(xp), '-',  xp2, p2(xp2), '-',color='orange')
_ = plt.plot( xxp, pp(xxp), '-',  xxp2, pp2(xxp2), '-',color='blue')
_ = plt.plot(nxx,nyy,'*',nx, ny, '.', color = 'red')
plt.legend(['experiment direct'])

plt.ylim(-0.1,0.5)
plt.xlim(0.5,1.5)
p4, v4 = np.polyfit(nx, ny, deg=1, cov=True)
print(p4)
print(v4)

plt.show()
