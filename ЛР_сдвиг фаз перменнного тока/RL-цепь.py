import numpy as np
import matplotlib.pyplot as plt
import math

def ctg(x):
    return 1 / math.tan(x)

plt.title('Зависимость ctg ψ = f(ω/LRΣ)')

plt.minorticks_on()
plt.grid(which='major',linewidth = 1,color = 'black',linestyle = '--')
plt.grid(which='minor',color = 'k',linestyle = ':')

plt.xlabel('ω/LRΣ', color='gray')
plt.ylabel('ctg ψ',color='gray')
nx = np.array([0,2000,4000,6000,8000,10000,11000])
nx = nx + 10 + 332#RΣ
nx = nx / (2 * math.pi * (10**3) * 0.5) #RΣ/ωL
ny = np.array([0.44,0.29,0.2,0.16,0.125,0.09,0.08])
for i in range(len(ny)):
    ny[i] = ny[i] * math.pi
    ny[i] = ctg(ny[i])

z = np.polyfit(nx, ny, 1)
xp = np.linspace(0, 11, 100)
p = np.poly1d(z)
_ = plt.plot(nx, ny, '.', xp, p(xp), '-')
plt.legend(['experiment point','experimental direct'])
plt.ylim(-0.5,4.5)
plt.xlim(-0.5,4.5)
p4, v4 = np.polyfit(nx, ny, deg=1, cov=True)
print(p4)
print(v4)

plt.show()
