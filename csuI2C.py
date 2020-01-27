import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
import adafruit_mpl3115a2

def init():
	global i2c
	global fxos
	global fxas
	global mpl

	i2c = busio.I2C(board.SCL, board.SDA)
	fxos = adafruit_fxos8700.FXOS8700(i2c)
	fxas = adafruit_fxas21002c.FXAS21002C(i2c)
	mpl = adafruit_mpl3115a2.MPL3115A2(i2c)
	mpl.sealevel_pressure = 102250

def acquire():
	#print(type(fxos.accelerometer))
	#print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.accelerometer))
	#print('Magnetometer (uTesla): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.magnetometer))
	#print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope))
	mplVal = (mpl.pressure, mpl.altitude, mpl.temperature)
    
	return fxos.accelerometer, fxos.magnetometer, fxas.gyroscope, mplVal
