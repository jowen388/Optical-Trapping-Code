#!/usr/bin/env python

from gpiozero import MCP3008
import time

adc = MCP3008(channel=0)
voltage = 3.3*adc.value

#tend = time.time() + 20
#while time.time() <= tend:
#    print(adc.value)

samples = 1000
value = []

start_time = time.time()

for x in range(0, samples):
    value.append(float(adc.value))

elapsed_time = time.time() - start_time
samplerate = samples / elapsed_time
averagevalue = float(sum(value))/max(len(value), 1)

print("%d samples in %.3f seconds" % (samples, elapsed_time))
print("%.3f samples per second" % samplerate)
print("%.6fV average" % averagevalue)
