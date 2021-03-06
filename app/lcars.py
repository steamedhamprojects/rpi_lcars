from screens.test import TestScreen
from ui.ui import UserInterface
import config
import serial


touchReleased = True
touchDelegate = None 


def filterSerial(string):
		global touchReleased
		minX = 0.25
		minY = 0.25
		maxX = 4.4
		maxY = 3.9

		components = string.split(",")

		# First, make sure both X and Y are there 
		if len(components) == 2:
			x = components[0]
			y = components[1]

			# Then check if the touch is valid, or if the screen is at rest 
			if float(x) > minX and float(y) > minY:
				# A touch has occurred on the screen 

				# Then translate the voltages into floats from 0-1 
				xFloat = float(x) / maxX
				yFloat = float(y) / maxY

				if touchReleased == True:
					# If the previous touch has ended, return this touch and prevent further touches until release
					touchReleased = False 
					# print("VOLTAGE:")
					# print("X: " + str(x) + " Y: " + str(y))
					floats = {"xFloat" : xFloat, "yFloat" : yFloat}
					return floats
				else:
					return {}
			else:
				# No touch
				touchReleased = True 
				return {}
		else:
			return {}

def openSerialPort():
	try: 
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	except serial.SerialException: 
		print("Serial port not found. Aborting.")
		return None 
	else: 
		ser.flush()
		return ser 

if __name__ == "__main__":

	firstScreen = TestScreen()
	ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
					   config.SOUND)

	ser = openSerialPort()
	touchDelegate = firstScreen

	while (True):
		ui.tick()

		if ser != None:
			if ser.in_waiting > 0:
				line = ser.readline().decode('utf-8').rstrip()
				touchLocation = filterSerial(line)


				if len(touchLocation) == 2:
					x = float(touchLocation["xFloat"])
					y = float(touchLocation["xFloat"])

					point = {"xFloat" : touchLocation["xFloat"], "yFloat" : touchLocation["yFloat"]}

					if touchLocation != None:
						ui.receiveTouch(point)


























