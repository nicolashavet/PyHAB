# PyHAB
# WRITTEN BY: Arko at EMFCAMP 2016 - HABVILLE

import pyb
from pyb import UART
from pyb import SPI

import RFM69
from RFM69Dict import registers, config

state = "RESET";

# Initialize perpherial variables
uart = UART(1, 9600)
#spi = SPI(1, SPI.MASTER, baudrate=1000000, polarity=0, phase=0, firstbit=SPI.MSB, crc=None)
rfm69 = RFM69.RFM69()

led = pyb.LED(4)
led.toggle()
pyb.delay(250)
led.toggle()
pyb.delay(250)
led.toggle()

def fault(*args):
    global state
    print ("Fault!")
    print ("Rebooting...")
    state = "RESET"
    return "RESET"

def reset():
	print ("Restarting...")
	return "INIT"

def init():
	print ("Initializing")

	# Initialize GPS
	# UART(1) is on PB: 
	# (TX,  RX) 
	# (X9,  X10)
	# (PB6, PB7)
	uart = UART(1, 9600)
	# Maybe add read_buf_len=128?
	# Maybe add timeout_char=200
	uart.init(9600, bits=8, stop=1, parity=None, timeout=5000)


	# Initialize Radio (RFM69)
	# SPI(1) is on PA:
	# (DIO0, RESET, NSS, SCK, MISO, MOSI) 
	# (X3,   X4,    X5,  X6,  X7,   X8) 
	# (PA2,  PA3,   PA4, PA5, PA6,  PA7)
	rfm69 = RFM69.RFM69()

	# Check version
	if (rfm69.getVersion() == 0x24):
		print ("RFM69 Version Valid: 0x24")
	else:
		print ("RFM69 Version Invalid!")
		return "FAULT"

	data = bytearray(3)
	data[0] = 5
	data[1] = 8
	data[2] = 9
	rfm69.send(data, 3, 15)

	return "GPS_ACQ"

def gps_acq():
	print ("Acquiring GPS data")

	# Default GPS Data is 8 lines
	#print (uart.readline())	#GNVTG
	#print (uart.readline()) #GNGGA
	#print (uart.readline()) #GNGSA
	#print (uart.readline()) #GNGSA
	#print (uart.readline()) #GPGSV
	#print (uart.readline()) #GPGSV
	#print (uart.readline()) #GNGLL
	#print (uart.readline()) #GNRMC

	return "PARSE_GPS"

def parse_gps():
	print ("Parsing GPS data")

	print ("Temperature: %d" % rfm69.readTemp())
	
	while (True):
		pass # HALT AND CATCH FIRE

	return "TRANSMIT"

def transmit():
	print ("Transmitting position and telemetry")
	return "GPS_ACQ"

states = {
		"FAULT": fault,
		"RESET": reset,
		"INIT": init, 
		"GPS_ACQ": gps_acq,
		"PARSE_GPS": parse_gps, 
		"TRANSMIT": transmit
}

# Semi-Safe State Machine?
while (True):
	state = states.get(state, fault)()
	print (state)

