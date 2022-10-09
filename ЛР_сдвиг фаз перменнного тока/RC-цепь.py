
import numpy as np
import matplotlib.pyplot as plt
import math

def ctg(x):
    return 1 / math.tan(x)

plt.title('Зависимость ctg ψ = f(ωCRΣ)')
plt.xlabel('ωCRΣ', color='gray')
plt.ylabel('ctg ψ',color='gray')
plt.minorticks_on()
plt.grid(which='major',linewidth = 1,color = 'black',linestyle = '--')
plt.grid(which='minor',color = 'k',linestyle = ':')

nx = np.array([0,540,1080,1620,2160,2700,3180])
nx = nx + 10 #RΣ
nx = nx * (2 * math.pi * (10**3) * 0.5 * (10**(-6))) #ωCRΣ
ny = np.array([0.48,0.18,0.09,0.06,0.055,0.049,0.048])
for i in range(len(ny)):
    ny[i] = ny[i] * math.pi
    ny[i] = ctg(ny[i])

z = np.polyfit(nx, ny, 1)
xp = np.linspace(0, 11, 100)
p = np.poly1d(z)
_ = plt.plot(nx, ny, '.', xp, p(xp), '-')
plt.legend(['experiment point','experimental direct'])
plt.ylim(-0.5,8)
p4, v4 = np.polyfit(nx, ny, deg=1, cov=True)
print(p4)
print(v4)

plt.show()
