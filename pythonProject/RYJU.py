import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots()
ax = fig.add_subplot(111, projection='3d')



initial_slope = 1

z = np.linspace(0, 100, 1000)
rp = z*initial_slope*np.cos(z*initial_slope)
x = z*initial_slope*np.sin(z*initial_slope)
y = z*initial_slope*np.cos(z*initial_slope)


plt.title('Slope Changer')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

Axcolor = '#0000FF'
Slope_slider = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor=Axcolor)
Slid = Slider(Slope_slider, 'Slope', 0.1, 1, valinit=1)

ax.plot(x, y)
def change(val):
    initial_slope = Slid.val
    z = np.linspace(0, 100, 1000)
    rp =z*initial_slope*np.cos(z*initial_slope)
    x = z*initial_slope*np.sin(z*initial_slope)
    y = z*initial_slope*np.cos(z*initial_slope)


    ax.clear()

    plot = ax.plot(x, y, rp, color='b')

    plt.title('Slope Changer')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')

    fig.canvas.draw_idle()

Slid.on_changed(change)
plt.show()