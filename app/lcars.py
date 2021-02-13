from screens.test import TestScreen
from ui.ui import UserInterface
import config
import serial


touchReleased = True

def filterSerial(string):
		global touchReleased
		minX = 0.25
		minY = 0.25

		components = string.split(",")

		if touchReleased == True and len(components) == 2:
			x = components[0]
			y = components[1]
			if x > minX and y > minY:
				# we have a valid press 
				return components
			else:
				touchReleased = true 
				return
		else:
			return 
		return 



if __name__ == "__main__":

	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	ser.flush()

	firstScreen = TestScreen()
	ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
					   config.SOUND)

	while (True):
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			touchLocation = filterSerial(line)
			print(touchLocation)
		
		ui.tick()



