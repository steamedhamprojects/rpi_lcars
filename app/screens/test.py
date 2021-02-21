import sys
import pygame
import config

from ui import colours
from ui.utils.sound import Sound

from ui.widgets.lcars_widgets import LcarsHStrip
from ui.widgets.lcars_widgets import LcarsBlockSmall
from ui.widgets.lcars_widgets import LcarsBlockMedium
from ui.widgets.lcars_widgets import LcarsBlockLarge
from ui.widgets.lcars_widgets import LcarsElbow
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText
from ui.widgets.screen import LcarsScreen
from ui.widgets.lcars_widgets import LcarsButton

class TestScreen(LcarsScreen):

    def setup(self, all_sprites):

        if config.DEV_MODE:
            all_sprites.add(LcarsButton(colours.GREY_BLUE, (0, 770), "X", self.exitHandler, (30, 30)), layer=2)
        
        self.layer1 = all_sprites.get_sprites_from_layer(1)
        self.layer2 = all_sprites.get_sprites_from_layer(2)

        # Uncomment for fullscreen
        #DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # For some reason, coordinates are passed in as y,x

        pad = 5
        hpad = 10

        topLeftElbow = LcarsElbow(colours.PEACH, 1, (10, hpad - 1))
        all_sprites.add(topLeftElbow, layer=1)

        screenWidth = pygame.display.get_surface().get_width()
        remainingWidth = screenWidth - topLeftElbow.rect.width - (hpad * 2)

        t1 = LcarsHStrip(colours.PEACH, (11, topLeftElbow.nextObjCoordX(-1)), remainingWidth, "")
        all_sprites.add(t1, layer=1)

        l1 = LcarsBlockSmall(colours.ORANGE, (topLeftElbow.nextObjCoordY(pad), hpad), "MUSIC")
        all_sprites.add(l1, layer=1)

        l2 = LcarsBlockSmall(colours.RED_BROWN, (l1.nextObjCoordY(pad), hpad), "NAVIGATION")
        all_sprites.add(l2, layer=1)

        l3 = LcarsBlockSmall(colours.BLUE, (l2.nextObjCoordY(pad), hpad), "PERFORMANCE")
        all_sprites.add(l3, layer=1)

        weather = LcarsImage("assets/weather.jpg", (l1.rect.y , l1.nextObjCoordX(10)))
        all_sprites.add(weather, layer=2)

        # b1 = LcarsHStrip(colours.PEACH, (400, hpad), 200, "")
        # all_sprites.add(b1, layer=1)

        # bottomRightElbow = LcarsElbow(colours.PEACH, 2, (250, 250))
        # all_sprites.add(bottomRightElbow, layer=1)

        # l2 = LcarsBlockMedium(colours.GREY_BLUE, (10, 10), "MEDIUM")
        # all_sprites.add(l2, layer=1)
        # l3 = LcarsBlockLarge(colours.PURPLE, (120, 10), "LARGE")
        # all_sprites.add(l3, layer=1)


        # sounds
        Sound("assets/audio/panel/215.wav").play()
        self.sound_granted = Sound("assets/audio/accessing.wav")
        self.sound_beep1 = Sound("assets/audio/panel/201.wav")
        self.sound_denied = Sound("assets/audio/access_denied.wav")
        self.sound_deny1 = Sound("assets/audio/deny_1.wav")
        self.sound_deny2 = Sound("assets/audio/deny_2.wav")

        self.reset()

    def reset(self):
        # Variables for PIN code verification
        self.correct = 0
        self.pin_i = 0
        self.granted = False
        for sprite in self.layer1: sprite.visible = True
        for sprite in self.layer2: sprite.visible = False

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Play sound
            self.sound_beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            self.sound_beep1.play()
            from screens.main import ScreenMain
            self.loadScreen(ScreenMain())

        # if event.type == pygame.MOUSEBUTTONUP:
        #     if (not self.layer2[0].visible):
        #         for sprite in self.layer1: sprite.visible = False
        #         for sprite in self.layer2: sprite.visible = True
        #         Sound("assets/audio/enter_authorization_code.wav").play()
        #     elif (self.pin_i == len(str(config.PIN))):
        #         # Ran out of button presses
        #         if (self.correct == len(config.PIN)):
        #             self.sound_granted.play()
        #             from screens.main import ScreenMain
        #             self.loadScreen(ScreenMain())
        #         else:
        #             self.sound_deny2.play()
        #             self.sound_denied.play()
        #             self.reset()

        return False


    def exitHandler(self, item, event, clock):
        sys.exit()
