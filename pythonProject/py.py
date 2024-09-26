import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots()
ax = fig.add_subplot(111,projection= '3d')

first_freq = 1
first_amp = 1

theta = np.linspace(0, np.pi*2, 100)
phi = np.linspace(0, np.pi, 100)


r = np.linspace(0, 1, 100)
x = r*np.sin(phi)*np.cos(theta)
y = r*np.sin(phi)*np.sin(theta)
z = r*np.cos(phi)

plot = ax.plot(x, y, z, color='b')

ax.set_title('3d Spherical Function With Sliders')
ax.set_ylabel('X Axis')
ax.set_xlabel('Y Axis')
ax.set_zlabel('Z Axis')

axcolor = 'lightgoldenrodyellow'
ax_freq = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_amp = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)

Freq =Slider(ax_freq,'Frequency', 0.1, 10, valinit=first_freq)
Amp =Slider(ax_amp, 'Amplitude', 0.1, 10, valinit=first_amp)
line, = ax.plot(x, y, z, lw=2)

def update(val):
    freq = Freq.val
    amp = Amp.val

    x = amp*r*np.sin(phi)*np.cos(freq*theta)
    y = amp*r*np.sin(phi)*np.sin(freq*theta)
    z = amp*r*np.cos(phi)

    ax.clear()

    plot = ax.plot(x, y, z, color='b')

    ax.set_title('3d Spherical Function With Sliders')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    fig.canvas.draw_idle()

Freq.on_changed(update)
Amp.on_changed(update)

plt.show()

