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
              #note to self - 0.035W finish ish

# create an instance of the ADCDAC Pi with a DAC gain set to 1
adcdac = ADCDACPi(1)
# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.31)

voltages1 = []
voltages2 = []  

starttime = time.time()
#************************************************

TIME = 0.1
NAME = 'wirepass6..'

#************************************************


while time.time() <= starttime + TIME:
    voltages1.append(adcdac.read_adc_voltage(1, 0))
    voltages2.append(adcdac.read_adc_voltage(2, 0))

def moving_average(a, n) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n] 
    return ret[n - 1:] / n

gaus10 = [0.196, 0.387, 0.704, 1.185, 1.839, 2.636, 3.448, 4.261, 4.804, 5]    #y=5e^{-0.04x^{2}}

                 
ave1 = []
ave2 = []

for i, x in enumerate(voltages1, 1):
    if i > 9:  
        ave1.append((x*gaus10[9] + voltages1[i-1]*gaus10[8] + voltages1[i-2]*gaus10[7] + voltages1[i-3]*gaus10[6] + voltages1[i-4]*gaus10[5] + voltages1[i-5]*gaus10[4] + voltages1[i-6]*gaus10[3] + voltages1[i-7]*gaus10[2] + voltages1[i-8]*gaus10[1] + voltages1[i-9]*gaus10[0])/(sum(gaus10)))

for i, x in enumerate(voltages2, 1):
    if i > 9:  
        ave2.append((x*gaus10[9] + voltages2[i-1]*gaus10[8] + voltages2[i-2]*gaus10[7] + voltages2[i-3]*gaus10[6] + voltages2[i-4]*gaus10[5] + voltages2[i-5]*gaus10[4] + voltages2[i-6]*gaus10[3] + voltages2[i-7]*gaus10[2] + voltages2[i-8]*gaus10[1] + voltages2[i-9]*gaus10[0])/(sum(gaus10)))

with open('volt' + NAME + '1.txt', 'w+') as f:
    for i in voltages1:
        f.write(str(i) + "\n")

with open('ave' + NAME + '1.txt', 'w+') as g:
      for i in ave1:
        g.write(str(i) + "\n")

with open('volt' + NAME + '2.txt', 'w+') as f:
    for i in voltages2:
        f.write(str(i) + "\n")

with open('ave' + NAME + '2.txt', 'w+') as g:
      for i in ave2:
        g.write(str(i) + "\n")


length = len(voltages1)
interval = TIME / length
timings = []
n = 0
for i in voltages1:
    timings.append(n*interval)
    n+=1

with open('time' + NAME + 'txt', 'w+') as h:
    for i in timings:
        h.write(str(i) + '\n')

        

plt.plot(timings[9:],ave1)
plt.plot(timings[9:],ave2)
#plt.plot(timings, voltages1)  
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

#plt.savefig(NAME + '.png')
plt.show()



