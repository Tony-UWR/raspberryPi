# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import matplotlib.pyplot as plt
import time
import board
import adafruit_dht
from drawnow import *

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D14,use_pulseio=False)


tempC=[]
humidity=[]
plt.ion()
def makeFig():
    plt.ylim(20,30)
    plt.title('Real Time DHT11 data')
    plt.grid(True)
    plt.ylabel('Temp C')
    plt.plot(tempC,'b^-',label='Degree C')
    plt.legend(loc='upper right')
    plt2=plt.twinx()
    plt.ylim(50,70)
    plt2.plot(humidity,'g*-',label='Humidity')
    plt2.set_ylabel('Humidity')
    plt2.ticklabel_format(useOffset=False)
    plt2.legend(loc='upper left')

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

count=0
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity_dht = dhtDevice.humidity
        tempC.append(round(temperature_c))
        humidity.append(round(humidity_dht))
        drawnow(makeFig)
        plt.pause(0.000001)
        count=count+1
        if(count>20):
            tempC.pop(0)
            humidity.pop(0)
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
