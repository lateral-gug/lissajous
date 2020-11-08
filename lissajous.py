import numpy as np
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time as tm
start = tm.time()

#x and y motion parameters
px = [1,6,0]
py = [1,8,np.pi/2]

#dampening coefficients
xdamp = 0.02
ydamp = 0.02

#animation parameters
time = 2*np.pi*10
frames = 10000
interval = 2

#curve plot parameters
opacity = 1
width = 0.5

def fx(t):
    return px[0]*np.exp(-xdamp*t)*np.cos(px[1]*t+px[2])

def fy(t):
    return py[0]*np.exp(-ydamp*t)*np.cos(py[1]*t+py[2])

xx = yy = np.array([])

t = np.linspace(0,time,frames)

for n, t in enumerate(t):
    x = fx(t)
    y = fy(t)
    xx = np.append(xx,x)
    yy = np.append(yy,y)

#static plot
fig1 = plt.figure(1,(5,5))
plt.plot(xx,yy,'r-',alpha=opacity,linewidth=width)

#dynamic plot
fig2 = plt.figure(2,(5,5))
dot, = plt.plot(xx,yy,'k.',markersize=15,zorder=3)
curve, = plt.plot(xx,yy,'r-',alpha=opacity,linewidth=width)

def animate(i):
    curve.set_data(xx[:i],yy[:i])
    dot.set_data(xx[i],yy[i])
    return curve, dot

video = anim.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True, repeat=True)

print(tm.time()-start)

#plt.grid(linestyle=':')

plt.show()
