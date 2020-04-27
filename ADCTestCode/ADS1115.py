#!/usr/bin/env python

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
'''
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)
samples = 1000
value = []

start_time = time.time()

for x in range(0, samples):
    value.append(float(chan.value))

elapsed_time = time.time() - start_time
samplerate = samples / elapsed_time
averagevalue = float(sum(value))/max(len(value), 1)

print("%d samples in %.3f seconds" % (samples, elapsed_time))
print("%.3f samples per second" % samplerate)
print("%.6fV average" % averagevalue)

'''

# Data collection setup
RATE = 860      #for 1115 8, 16, 32, 64, 128, 250, 475, 860
SAMPLES = 1000

# Create the I2C bus with a fast frequency
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)

# ADC Configuration
ads.data_rate = RATE     
data = [None]*SAMPLES

start = time.monotonic()

# Read the same channel over and over
for i in range(SAMPLES):
    data[i] = chan0.value

end = time.monotonic()
total_time = end - start

print("Time of capture: {}s".format(total_time))
print("Sample rate requested={} actual={}".format(RATE, SAMPLES / total_time))
