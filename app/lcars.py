from screens.test import TestScreen
from ui.ui import UserInterface
import config

if __name__ == "__main__":
    firstScreen = TestScreen()
    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE,
                       config.SOUND)

    while (True):
        ui.tick()
