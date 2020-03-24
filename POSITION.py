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
from math import sqrt              
              

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
NAME ='test'

#************************************************

# 2.23 for board 10
# 1.074 - board 11
offset = 1


while time.time() <= starttime + TIME:
    voltages1.append(adcdac.read_adc_voltage(1, 0)*offset)

    voltages2.append(adcdac.read_adc_voltage(2, 0))
def moving_average(a, n) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n] 
    return ret[n - 1:] / n

gaus10 = [0.196, 0.387, 0.704, 1.185, 1.839, 2.636, 3.448, 4.261, 4.804, 5]    #y=5e^{-0.04x^{2}}

                 
gwma1 = []
gwma2 = []

for i, x in enumerate(voltages1, 1):
    if i > 9:  
        gwma1.append((x*gaus10[9] + voltages1[i-1]*gaus10[8] + voltages1[i-2]*gaus10[7] + voltages1[i-3]*gaus10[6] + voltages1[i-4]*gaus10[5] + voltages1[i-5]*gaus10[4] + voltages1[i-6]*gaus10[3] + voltages1[i-7]*gaus10[2] + voltages1[i-8]*gaus10[1] + voltages1[i-9]*gaus10[0])/(sum(gaus10)))

for i, x in enumerate(voltages2, 1):
    if i > 9:  
        gwma2.append((x*gaus10[9] + voltages2[i-1]*gaus10[8] + voltages2[i-2]*gaus10[7] + voltages2[i-3]*gaus10[6] + voltages2[i-4]*gaus10[5] + voltages2[i-5]*gaus10[4] + voltages2[i-6]*gaus10[3] + voltages2[i-7]*gaus10[2] + voltages2[i-8]*gaus10[1] + voltages2[i-9]*gaus10[0])/(sum(gaus10)))

#with open(NAME + 'volt' + '1.txt', 'w+') as f:
#    for i in voltages1:
#        f.write(str(i) + "\n")

with open(NAME +'gwma' +  '1.txt', 'w+') as g:
      for i in gwma1:
        g.write(str(i) + "\n")

#with open(NAME +'volt'  + '2.txt', 'w+') as f:
#    for i in voltages2:
#        f.write(str(i) + "\n")

with open(NAME +'gwma' + '2.txt', 'w+') as g:
      for i in gwma2:
        g.write(str(i) + "\n")



position = [3.92*(x-y)/(x+y) for x, y in zip(gwma1, gwma2)] # half psd length 1.75 * calibration 2.34

with open(NAME +'position' + '.txt', 'w+') as g:
      for i in position:
        g.write(str(i) + "\n")



length = len(voltages1)
interval = TIME / length
timings = []
n = 0
for i in voltages1:
    timings.append(n*interval)
    n+=1

with open( NAME + 'time.txt', 'w+') as h:
    for i in timings:
        h.write(str(i) + '\n')



def rmse(data, average):
    diffsq= []
    for x in data:
        diffsq.append((x-average)*(x-average))
    return(sqrt(sum(diffsq)/len(diffsq))) 
        

avegwma1 = np.mean(gwma1)
rmsegwma1 = rmse(gwma1, avegwma1)
avegwma2 = np.mean(gwma2)
rmsegwma2 = rmse(gwma2, avegwma2)
aveposition = np.mean(position)
rmseposition = rmse(position, aveposition)

with open(NAME + 'aveserrors.txt', 'w+') as h:
    h.write('Ave GWMA 1: ' + str(avegwma1) + '\n' + 'RMSE GWMA 1: ' + str(rmsegwma1) + '\n' + 'Ave GWMA 2: ' + str(avegwma2) + '\n' + 'RMSE GWMA 2: ' + str(rmsegwma2) + '\n' +'Ave Position: ' + str(aveposition) + '\n' + 'RMSE Position: ' + str(rmseposition))
    
    



plt.plot(timings[9:],gwma1)
#plt.plot(timings[9:],gwma2)
#plt.plot(timings, voltages1)
#plt.plot(timings, voltages2)  
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

#plt.savefig(NAME + '.png')
plt.show()



