# Simple demo of setting the output voltage of the MCP4725 DAC.
# Will alternate setting 0V, 1/2VDD, and VDD each second.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the MCP4725 module.
import Adafruit_MCP4725

# Create a DAC instance.
dac = Adafruit_MCP4725.MCP4725()

# Note you can change the I2C address from its default (0x62), and/or the I2C
# bus by passing in these optional parameters:
#dac = Adafruit_MCP4725.MCP4725(address=0x49, busnum=1)

# Loop forever alternating through different voltage outputs.
print('Press Ctrl-C to quit...')
while True:
    print('Setting voltage to 0!')
    dac.set_voltage(0)
    time.sleep(2.0)
    print('Setting voltage to 1/2 Vdd!')
    dac.set_voltage(2048)  # 2048 = half of 4096
    time.sleep(2.0)
    print('Setting voltage to Vdd!')
    dac.set_voltage(4096, True)
    time.sleep(2.0)
