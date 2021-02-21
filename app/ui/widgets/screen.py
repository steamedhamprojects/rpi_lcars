import pygame
class LcarsScreen:
    """
    Manage a UI screen
    """
    def __init__(self):
        self.nextScreen = None
        self.lastFrameTicks = 0
    
    def setup(self):
        """
        Set up the screen widgets. self.params may contain parameters if 
        passed from previous screen
        """
        pass

    # def hitTest(self, coordinates):
    #     print("Performing hit test on" + coordinates)

    #     for view in all_sprites.sprites():
    #         # if coordinates are inside the rect of the view, return the view 
    #         if view.rect.contains(Rect(coordinates[x], coordinates[y], 1, 1)) == True:
    #             view .handleEvent(pygame.event.Event(pygame.MOUSEBUTTONUP))
    #             return 


    def getDeltaTime(self, fpsClock):
        """
        Return the amount of time in milliseconds since last frame 
        """
        t = pygame.time.get_ticks()
        deltaTime = (t - self.lastFrameTicks)
        self.lastFrameTicks = t
        return deltaTime
    
    def pre_update(self, screenSurface, fpsClock):
        """
        Called every frame to run any UI updates, before widgets are drawn 
        """
        pass

    def update(self, screenSurface, fpsClock):
        """
        Called every frame to run any UI updates, after widgets are drawn 
        """
        pass
    
    def handleEvents(self, event, fpsClock):
        """
        Called when an event occurs 
        """
        return False
    
    def loadScreen(self, newScreen, params={}):
        """
        Queue up the next screen to load. 
        """
        self.nextScreen = newScreen
        self.nextScreen.params = params
        
    def getNextScreen(self):
        """
        Returns the screen queued up to load next. The screen is popped off the
        1-level stack, so only call this method once per screen  
        """
        nextScreen = self.nextScreen
        self.nextScreen = None
        return nextScreen