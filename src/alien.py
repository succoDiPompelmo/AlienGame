import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set his starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and get its rect
        self.image = pygame.image.load("../img/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def update(self):
        """The aliens move from a side to side changing direction when it reaches the borders"""
        self.rect.centerx += 1

    def blitme(self):
        """Draw the alien at his current location"""
        # If we use the method draw from the Sprite class this line is useless but we keep the
        # possibilities to draw a single alien outside the Sprite Group with this
        self.screen.blit(self.image, self.rect)
