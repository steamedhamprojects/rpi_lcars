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

    all_sprites = []

    def convertFloatToPoints(self, x=float, y=float):

        screenWidth = pygame.display.get_surface().get_width()
        screenHeight = pygame.display.get_surface().get_height()

        return (int(x * screenWidth), int(y * screenHeight))

    def yPercToPoints(self, y):

        screenHeight = pygame.display.get_surface().get_height()
        return int(y * screenHeight)

    def xPercToPoints(self, x):

        screenWidth = pygame.display.get_surface().get_width()
        return int(x * screenWidth)

    def convertScreenHeightPointsToFloat(self, y):
        screenHeight = pygame.display.get_surface().get_height()
        return y / screenHeight

    def convertScreenWidthPointsToFloat(self, x):
        screenWidth = pygame.display.get_surface().get_width()
        return x / screenWidth

    def setup(self, all_sprites):

        if config.DEV_MODE:
            all_sprites.add(LcarsButton(colours.GREY_BLUE, (0, 770), "X", self.exitHandler, (30, 30)), layer=2)
        
        self.layer1 = all_sprites.get_sprites_from_layer(1)
        self.layer2 = all_sprites.get_sprites_from_layer(2)

        self.all_sprites = all_sprites

        # Uncomment for fullscreen
        #DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # For some reason, coordinates are passed in as y,x

        pad = 5
        hpad = 10

        leftStackWidth = 0.1345
        screenWidth = pygame.display.get_surface().get_width()
        screenHeight = pygame.display.get_surface().get_height()

        # Elbow
        topLeftElbow = LcarsElbow(colours.PEACH, 0, (-40, hpad - 1), self.convertFloatToPoints(x = 0.3, y = 0.15)) #0.225
        all_sprites.add(topLeftElbow, layer=1)

        # Second elbow
        secondElbow = LcarsElbow(colours.PEACH, 1, (topLeftElbow.nextObjCoordY(pad), hpad - 1), self.convertFloatToPoints(x = 0.3, y = 0.15)) #0.225
        all_sprites.add(secondElbow, layer=1)

        # First Horizontal Bar
        h1 = LcarsHStrip(colours.PEACH, (self.yPercToPoints(0.0595), topLeftElbow.nextObjCoordX(pad)), 60, self.yPercToPoints(0.035), "")
        all_sprites.add(h1, layer=1)

        h2 = LcarsHStrip(colours.ORANGE, (self.yPercToPoints(0.0595), h1.nextObjCoordX(pad)), 120, self.yPercToPoints(0.035), "")
        all_sprites.add(h2, layer=1)

        h3 = LcarsHStrip(colours.PEACH, (self.yPercToPoints(0.0595), h2.nextObjCoordX(pad)), 20, self.yPercToPoints(0.035), "")
        all_sprites.add(h3, layer=1)

        h4 = LcarsHStrip(colours.ORANGE, (self.yPercToPoints(0.0595), h3.nextObjCoordX(pad)), 50, self.yPercToPoints(0.035), "")
        all_sprites.add(h4, layer=1)

        h5 = LcarsHStrip(colours.PEACH, (self.yPercToPoints(0.0595), h4.nextObjCoordX(pad)), 140, self.yPercToPoints(0.035), "")
        all_sprites.add(h5, layer=1)

        h6 = LcarsHStrip(colours.ORANGE, (self.yPercToPoints(0.0595), h5.nextObjCoordX(pad)), 20, self.yPercToPoints(0.035), "")
        all_sprites.add(h6, layer=1)

        remainingWidth = screenWidth - h6.rect.left - h6.rect.width - (hpad * 2)
        hlast = LcarsHStrip(colours.PEACH, (self.yPercToPoints(0.0595), h6.nextObjCoordX(pad)), remainingWidth - pad, self.yPercToPoints(0.035), "")
        all_sprites.add(hlast, layer=1)

        # Second Horizontal Bar 
        h7 = LcarsHStrip(colours.PEACH, (secondElbow.rect.top + 1, secondElbow.nextObjCoordX(0)), 40, self.yPercToPoints(0.035), "")
        all_sprites.add(h7, layer=1)

        h8 = LcarsHStrip(colours.ORANGE, (h7.rect.top, h7.nextObjCoordX(pad)), 240, self.yPercToPoints(0.035), "")
        all_sprites.add(h8, layer=1)

        h9 = LcarsHStrip(colours.PEACH, (h7.rect.top, h8.nextObjCoordX(pad)), 30, self.yPercToPoints(0.035), "")
        all_sprites.add(h9, layer=1)

        h10 = LcarsHStrip(colours.ORANGE, (h7.rect.top, h9.nextObjCoordX(pad)), 90, self.yPercToPoints(0.035), "")
        all_sprites.add(h10, layer=1)

        h11 = LcarsHStrip(colours.PEACH, (h7.rect.top, h10.nextObjCoordX(pad)), 100, self.yPercToPoints(0.035), "")
        all_sprites.add(h11, layer=1)

        h12 = LcarsHStrip(colours.ORANGE, (h7.rect.top, h11.nextObjCoordX(pad)), 75, self.yPercToPoints(0.035), "")
        all_sprites.add(h12, layer=1)

        secondRemainingWidth = screenWidth - h12.rect.left - h12.rect.width - (hpad * 2)
        secondHLast = LcarsHStrip(colours.PEACH, (h7.rect.top, h12.nextObjCoordX(pad)), secondRemainingWidth - pad, self.yPercToPoints(0.035), "")
        all_sprites.add(secondHLast, layer=1)

        # Left Menu Stack
        l1 = LcarsBlockSmall(colours.ORANGE, (secondElbow.nextObjCoordY(pad), hpad), "MEDIA", self.convertFloatToPoints(x=leftStackWidth, y=0.10))
        l1.handler = self.musicHandler
        all_sprites.add(l1, layer=1)

        l2 = LcarsBlockSmall(colours.RED_BROWN, (l1.nextObjCoordY(pad), hpad), "COMMUNICATION", self.convertFloatToPoints(x=leftStackWidth, y=0.10))
        all_sprites.add(l2, layer=1)

        l3 = LcarsBlockSmall(colours.DARK_BLUE, (l2.nextObjCoordY(pad), hpad), "NAVIGATION", self.convertFloatToPoints(x=leftStackWidth, y=0.10))
        all_sprites.add(l3, layer=1)

        l4 = LcarsBlockSmall(colours.RED, (l3.nextObjCoordY(pad), hpad), "PERFORMANCE", self.convertFloatToPoints(x=leftStackWidth, y=0.075))
        all_sprites.add(l4, layer=1)

        l5 = LcarsBlockSmall(colours.BLUE, (l4.nextObjCoordY(pad), hpad), "ENGINEERING", self.convertFloatToPoints(x=leftStackWidth, y=0.075))
        all_sprites.add(l5, layer=1)

        # Variable height spacer 
        bottomElbowHeight = 0.15
        remainingHeight = screenHeight - l5.rect.top - l5.rect.height - self.yPercToPoints(bottomElbowHeight) - (hpad * 2)
        bottomLeftSpacer = LcarsBlockSmall(colours.WHITE, (l5.nextObjCoordY(pad), hpad), "", self.convertFloatToPoints(x = leftStackWidth, y = self.convertScreenHeightPointsToFloat(remainingHeight)))
        all_sprites.add(bottomLeftSpacer, layer=1)

        # Bottom Left Elbow
        bottomLeftElbow = LcarsElbow(colours.PEACH, 0, (bottomLeftSpacer.nextObjCoordY(pad), l5.rect.left), self.convertFloatToPoints(x = 0.3, y = bottomElbowHeight)) #0.225
        all_sprites.add(bottomLeftElbow, layer=1)

        # Bottom Horizontal Bar
        h13 = LcarsHStrip(colours.PEACH, (self.yPercToPoints(0.95), bottomLeftElbow.nextObjCoordX(pad)), self.yPercToPoints(0.1), self.yPercToPoints(0.035), "")
        all_sprites.add(h13, layer=1)

        # Variable width spacer
        bottomRightElbowWidth = 0.3
        bottomRemainingWidth = screenWidth - h13.rect.left - h13.rect.width - self.xPercToPoints(bottomRightElbowWidth) - (hpad * 2)
        bottomRightSpacer = LcarsBlockSmall(colours.WHITE, (h13.rect.top, h13.nextObjCoordX(pad)), "", self.convertFloatToPoints(x = self.convertScreenWidthPointsToFloat(bottomRemainingWidth), y = 0.035))
        all_sprites.add(bottomRightSpacer, layer=1)

        # Bottom Right Elbow
        bottomRightElbow = LcarsElbow(colours.PEACH, 3, (bottomRightSpacer.rect.top, bottomRightSpacer.nextObjCoordX(pad)), self.convertFloatToPoints(x = bottomRightElbowWidth, y = bottomElbowHeight)) #0.225
        all_sprites.add(bottomRightElbow, layer=1)


        # weather = LcarsImage("assets/weather.jpg", (l1.rect.y , l1.nextObjCoordX(10)))
        # all_sprites.add(weather, layer=2)

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

    def musicHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Play sound
            self.sound_beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            self.sound_beep1.play()

            # l2 = LcarsBlockSmall(colours.RED_BROWN, (event.pos[1], event.pos[0]), "Hit")
            # self.all_sprites.add(l2, layer=1)

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
