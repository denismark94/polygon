import random
from collections import deque

import matplotlib.pyplot as plt 
import matplotlib.animation as animation

npoints = 100
x = deque([0], maxlen=npoints)
y = deque([0], maxlen=npoints)
fig, ax = plt.subplots()
[line] = ax.step(x, y)

def update(dy):
    x.append(x[-1] + 1)  # обновить данные
    y.append(y[-1] + dy)

    line.set_xdata(x)  # обновить данные графика
    line.set_ydata(y)

    ax.relim()  # обновить пределы осей
    ax.autoscale_view(True, True, True)
    return line, ax


def data_gen():  # функция для ввода данных
    while True:
        yield 1 if random.random() < 0.5 else -1
        i = 1
        yield i
        

def update_send(dy):
    x2.append(x2[-1] + 1)  # обновить данные
    y2.append(y2[-1] + dy)

    line2.set_xdata(x2)  # обновить данные графика
    line2.set_ydata(y2)

    ax2.relim()  # обновить пределы осей
    ax2.autoscale_view(True, True, True)
    return line2, ax2

def update_get(dy):
    x3.append(x3[-1] + 1)  # обновить данные
    y3.append(y3[-1] + dy)

    line3.set_xdata(x3)  # обновить данные графика
    line3.set_ydata(y3)

    ax3.relim()  # обновить пределы осей
    ax3.autoscale_view(True, True, True)
    return line3, ax3

def update_average(dy):
    x4.append(x4[-1] + 1)  # обновить данные
    y4.append(y4[-1] + dy)

    line4.set_xdata(x4)  # обновить данные графика
    line4.set_ydata(y4)

    ax4.relim()  # обновить пределы осей
    ax4.autoscale_view(True, True, True)
    return line4, ax4

x2 = deque([0], maxlen=npoints)
y2 = deque([0], maxlen=npoints)
fig2, ax2 = plt.subplots()
[line2] = ax2.step(x2, y2)

x3 = deque([0], maxlen=npoints)
y3 = deque([0], maxlen=npoints)
fig3, ax3 = plt.subplots()
[line3] = ax3.step(x3, y3)

x4 = deque([0], maxlen=npoints)
y4 = deque([0], maxlen=npoints)
fig4, ax4 = plt.subplots()
[line4] = ax4.step(x4, y4)

ani = animation.FuncAnimation(fig, update, 1)

ani2 = animation.FuncAnimation(fig2, update_send, data_gen)

ani3 = animation.FuncAnimation(fig3, update_get, data_gen)

ani4 = animation.FuncAnimation(fig4, update_average, data_gen)

plt.show()