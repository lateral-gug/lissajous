import numpy as np
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#x and y parameters
px = [1,3,0.5]
py = [1,2,0]

#animation parameters
time = 100
frames = 10000
interval = 5

def fx(t):
    return px[0]*np.cos(px[1]*t+px[2])

def fy(t):
    return py[0]*np.cos(py[1]*t+py[2])

xx = yy = np.array([])

t = np.linspace(0,time,frm)

for n, t in enumerate(t):
    x = fx(t)
    y = fy(t)
    xx = np.append(xx,x)
    yy = np.append(yy,y)

def animate(i):
    redDot.set_data(xx[i],yy[i])
    return redDot,

fig = plt.figure()

plt.plot(xx,yy,'r-',alpha=0.2)

redDot, = plt.plot(xx,yy,'k.',markersize=15,zorder=3)

myAnimation1 = anim.FuncAnimation(fig, animate, frames=frm, interval=inter, blit=True, repeat=False)

plt.grid(linestyle=':')
plt.show()