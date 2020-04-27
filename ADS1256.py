#!/usr/bin/env python

import time
import board
import busio
import sys
from ADS1256_definitions import *
from pipyadc import ADS1256
import bench_config as conf

# Input pin for the potentiometer on the Waveshare Precision ADC board:
POTI = POS_AIN0|NEG_AINCOM
# Light dependant resistor of the same board:
LDR  = POS_AIN1|NEG_AINCOM
# Eight channels
CH_SEQUENCE = (POTI, LDR)
############################

SAMPLES=1000


ads = ADS1256(conf)
ads.cal_self()

for i in range(SAMPLES):
    data[i] = ads.read_continue(CH_SEQUENCE)

end = time.monotonic()
total_time = end - start

print("Time of capture: {}s".format(total_time))
print("Sample rate requested={} actual={}".format(RATE, SAMPLES / total_time))
