import time
import board
import busio
import serial
import adafruit_gps



def init():
	# for a computer, use the pyserial library for uart access
	global uart
	global gps
	uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)

	# Create a GPS module instance.
	gps = adafruit_gps.GPS(uart, debug=False)     # Use UART/pyserial

	# Turn on the basic GGA and RMC info (what you typically want)
	gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')


	# Set update rate to once a second (1hz) which is what you typically want.
	gps.send_command(b'PMTK220,1000')
	# This would be twice a second (2hz, 500ms delay):
	# gps.send_command(b'PMTK220,500')	

def acquire():
	# Simple GPS module demonstration.
	# Will wait for a fix and print a message every second with the current location
	# and other details.
	global gps
	global uart
	# Main loop runs forever printing the location, etc. every second.
	# Make sure to call gps.update() every loop iteration and at least twice
	# as fast as data comes from the GPS unit (usually every second).
	# This returns a bool that's true if it parsed new data (you can ignore it
	# though if you don't care and instead look at the has_fix property).
	gps.update()
	# Every second print out current location details if there's a fix.
	while not gps.has_fix:
		# Try again if we don't have a fix yet.
		gps.update()
		#continue
	# We have a fix! (gps.has_fix is true)
	# Print out details about the fix like location, date, etc.
	time = (gps.timestamp_utc.tm_hour, gps.timestamp_utc.tm_min, gps.timestamp_utc.tm_sec)
	#Data Tuple of (Latitude, Longitude, Altitude, Speed, TAD, HD)
	gpsData = (gps.latitude, gps.longitude, gps.altitude_m, gps.speed_knots, gps.track_angle_deg, gps.horizontal_dilution)
	gpsQuality = (gps.fix_quality, gps.satellites)
	
	#section that prints out Data
	# print('=' * 40)  # Print a separator line.
	# print('Fix timestamp: {0[0]:02}:{0[1]:02}:{0[2]:02} '.format(time))
	# print('Latitude: {0:.6f} degrees'.format(gps.latitude))
	# print('Longitude: {0:.6f} degrees'.format(gps.longitude))
	# print('Fix quality: {}'.format(gps.fix_quality))
	# Some attributes beyond latitude, longitude and timestamp are optional
	# and might not be present.  Check if they're None before trying to use!
	# if gps.satellites is not None:
	# 	print('# satellites: {}'.format(gps.satellites))
	# if gps.altitude_m is not None:
	# 	print('Altitude: {} meters'.format(gps.altitude_m))
	# if gps.speed_knots is not None:
	# 	print('Speed: {} knots'.format(gps.speed_knots))
	# if gps.track_angle_deg is not None:
	# 	print('Track angle: {} degrees'.format(gps.track_angle_deg))
	# if gps.horizontal_dilution is not None:
	# 	print('Horizontal dilution: {}'.format(gps.horizontal_dilution))
	# if gps.height_geoid is not None:
	# 	print('Height geo ID: {} meters'.format(gps.height_geoid))

	return time, gpsData, gpsQuality