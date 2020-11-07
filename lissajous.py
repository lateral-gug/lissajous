import numpy as np
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#x and y motion parameters
px = [1,5,0]
py = [1,3,np.pi/2]

#dampening coefficients
xdamp = 0.01
ydamp = 0.01

#animation parameters
time = 2*np.pi*7
frames = 10000
interval = 5
opacity = 0.7

def fx(t):
    return px[0]*np.exp(-xdamp*t)*np.cos(px[1]*t+px[2])

def fy(t):
    return py[0]*np.exp(-ydamp*t)*np.cos(py[1]*t+py[2])

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

plt.plot(xx,yy,'r-',alpha=opacity)

redDot, = plt.plot(xx,yy,'k.',markersize=15,zorder=3)

myAnimation1 = anim.FuncAnimation(fig, animate, frames=frm, interval=inter, blit=True, repeat=True)

plt.grid(linestyle=':')
plt.show()
