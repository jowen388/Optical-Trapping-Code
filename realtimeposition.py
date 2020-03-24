#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime
import time 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.lines import Line2D
from ADCDACPi import ADCDACPi
import matplotlib.animation as animation
from matplotlib.lines import Line2D
              

# create an instance of the ADCDAC Pi with a DAC gain set to 1
adcdac = ADCDACPi(1)
# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.31)

# 0.035 for board 10
#-0.148 for board 11       
offset = 2.23

class Scope(object):
    def __init__(self, ax, maxt=4, dt=0.01):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-5,5)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,


def emitter():
    while True:
            a = adcdac.read_adc_voltage(1, 0) *offset
            b = adcdac.read_adc_voltage(2, 0) 
            
            yield (((a-b)-2.8)*15)/(a+b)    # half psd length 1.75 * calibration 2.34
  




fig, ax = plt.subplots()
scope = Scope(ax)

# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, emitter, interval=10, blit=True)

#ani2 = animation.FuncAnimation(fig, scope.update, emitter, interval=10, blit=True)

plt.grid(True)
plt.show()






