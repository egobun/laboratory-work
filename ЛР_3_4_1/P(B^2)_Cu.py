from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import math
v0 = 1000
def ctg(x):
    return 1 / math.tan(x)

plt.title('Зависимость для Cu ΔP[Тл] = B^2[Tл^2] ')
x = np.array([0.3,0.67,1.00,1.41,1.80,2.15,2.53,2.81,3.03])
y = np.array([261,259,257,254,251,247,242,240,237])
y = y - 265
x = (x*0.27615443+0.02937324)**2
x1 = np.array([3.03,2.75,2.38,1.90,1.59,1.17,0.68,0.34,0.26])
y1 = np.array([237,241,245,250,253,256,259,260,261])
y1 = y1 - 265
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

_ = plt.plot(xp, p(xp),'C1-',xp1,p1(xp1),'m-',x, y, 'C1.',x1,y1,'m.')



plt.legend(['ΔФ>0','ΔФ<0'])


p4, v4 = np.polyfit(x, y, deg=1, cov=True)
print(p4)
print(v4)

plt.show()
