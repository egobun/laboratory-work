import numpy as np
import matplotlib.pyplot as plt
import math
v0 = 1000
def ctg(x):
    return 1 / math.tan(x)

plt.title('Зависимость B(Тл) = I(A) ')
x = np.array([0.28,0.68,1.00,1.42,1.82,2.14,2.50,2.84,3.01])
y = np.array([7,16,21,31,39,46,52,58,61])
print(y)
y = ((y/10) * 10**(-3))/(72 * 10**(-4))

plt.minorticks_on()
plt.grid(which='major',linewidth = 1,color = 'black',linestyle = '--')
plt.grid(which='minor',color = 'k',linestyle = ':')

plt.xlabel('I[A]', color='gray')
plt.ylabel('B[Тл]',color='gray')



z = np.polyfit(x, y, 1)
xp = np.linspace(0, 3, 100)
p = np.poly1d(z)
_ = plt.plot(x, y, '.', xp, p(xp), '-')

plt.legend(['experiment direct'])

#plt.ylim(-0.1,0.5)
#plt.xlim(0.5,1.5)
p4, v4 = np.polyfit(x, y, deg=1, cov=True)
print(p4)
print(v4)

plt.show()
