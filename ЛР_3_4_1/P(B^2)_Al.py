from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import math
v0 = 1000
def ctg(x):
    return 1 / math.tan(x)

strx = '0,27 0,73 0,98 1,33 1,67 2,2 2,58 2,81 3,03'
strx = strx.replace(',','.')
strx = strx.split(' ')
strx = [float(i) for i in strx]

strx1 = '3,03 2,74 2,57 2,02 1,76 1,21 0,9 0,68 0,31'
strx1 = strx1.replace(',','.')
strx1 = strx1.split(' ')
strx1 = [float(i) for i in strx1]

plt.title('Зависимость для Al ΔP[Тл] = B^2[Tл^2] ')
x = np.array([*strx])
y = np.array([1,4,7,11,19,26,35,42,47])
x = (x*0.27615443+0.02937324)**2
x1 = np.array([*strx1])
y1 = np.array([47,43,39,27,20,10,6,4,2])
x1 = (x1*0.27615443+0.02937324)**2
plt.minorticks_on()
plt.grid(which='major',linewidth = 1,color = 'black',linestyle = '--')
plt.grid(which='minor',color = 'k',linestyle = ':')

plt.xlabel('B^2[Тл^2]', color='gray')
plt.ylabel('ΔP[мг]',color='gray')



z = np.polyfit(x, y, 1)
xp = np.linspace(0, 0.8, 100)
p = np.poly1d(z)

z1 = np.polyfit(x1, y1, 1)
xp1 = np.linspace(0, 0.8, 100)
p1 = np.poly1d(z1)

_ = plt.plot(xp, p(xp), 'g-',xp1,p1(xp1),'r-',x, y, 'g.',x1,y1,'r.')



plt.legend(['ΔФ>0','ΔФ<0'])


p4, v4 = np.polyfit(x, y, deg=1, cov=True)
print(p4)
print(v4)

plt.show()
