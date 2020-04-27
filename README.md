# Optical-Trapping-Code

This is the code used to control a Raspberry Pi which reads the output from a position sensitive detector via the analogue to digital converter of the ADC-DAC Pi Zero sub board. 

### Prerequisites

If not already, the ADC-DAC Pi Zero software must be installed. Instructions from https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/blob/master/ADCDACPi/README.md
To download to your Raspberry Pi type in terminal:
```
git clone https://github.com/abelectronicsuk/ABElectronics_Python_Libraries.git
```
To install the python library navigate into the ABElectronics_Python_Libraries folder and run:

For Python 2.7:
```
sudo python setup.py install
```
For Python 3.5:
```
sudo python3 setup.py install
```
If you have PIP installed you can install the library directly from github with the following command:

For Python 2.7:
```
sudo python2.7 -m pip install git+https://github.com/abelectronicsuk/ABElectronics_Python_Libraries.git
```
For Python 3.5:
```
sudo python3.5 -m pip install git+https://github.com/abelectronicsuk/ABElectronics_Python_Libraries.git
```

## Running the tests

There are three main programs.

### 1. POSITION.py

To use this program, you can select the length of time you want the test to run for and the name which you would like the saved data to be called here:

```
#************************************************

TIME = 0.1
NAME ='name'

#************************************************
```
Once it has completed a run, the program will save 6 .txt files containing the data. These contain:
* two files with the guassian weighted moving averaged voltages measured across the two output channels of the PSD during the time frame (namegwma1.txt and namegwma2.txt) 
* one file with the calcualted postion of the object on the PSD (namepostion.txt)
* one file with the time data (nametime.txt)
* one file with detailing the as the averages and root mean square errors of the data (nameaveserrors.txt)

### 2. realtimeposition.py
This program plots the measured and position in real time, with a time step of 0.01s.
There is potential to change this time step although not advised, lengthening it removed details, shortening it increasing processing time and slows down the display.
To change dt, edit:

```
class Scope(object):
    def __init__(self, ax, maxt=4, dt=0.01):
 ```

### 3. realtime.py
The same code as realtimeposition.py but plots one of the singal output voltaged measured from the PSD.
To choose the channel, write 1 or 2 in the read_adc brackets.
```
def emitter2():
   while True:
            yield adcdac.read_adc_voltage(1, 0)
```

## ADC Testing codes

Series of codes used to test the maximum samples per second for a few ADCs. Most codes measured the time taken to carry out a known number of readings, which was then divided to find the number of reading taken per second. These codes were either directly copied or developed from their respective online directories lsited below.

https://github.com/abelectronicsuk/ABElectronics_Python_Libraries

https://github.com/adafruit/Adafruit_Python_ADS1x15

https://github.com/ul-gh/PiPyADC

https://github.com/adafruit/Adafruit_Python_MCP3008


## Authors

Code written by Jasmine Owen and Rebecca Rogers.

