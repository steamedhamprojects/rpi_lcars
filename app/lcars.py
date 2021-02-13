from screens.test import TestScreen
from ui.ui import UserInterface
import config
import serial

if __name__ == "__main__":

	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	ser.flush()

    firstScreen = TestScreen()
    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
                       config.SOUND)

    while (True):
        if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			print(line)

		ui.tick()
