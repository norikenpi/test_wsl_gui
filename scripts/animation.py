import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# アニメーションの描画領域を設定
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

# framesの範囲を拡張してより多くのフレームを生成
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 256), # フレーム数を増やす
                    init_func=init, blit=True)

# アニメーションを60fpsで保存
#ani.save('sine_wave_animation_smooth.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

plt.show()
