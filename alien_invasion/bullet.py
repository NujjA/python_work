import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    
    def __init__ (self, ai_settings, screen, ship):
        """create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.heihei = True
        
        #self.image = pygame.image.load('Moana_boat_small.bmp')

        if self.heihei:
            self.image = pygame.image.load('heihei_small.bmp')
            self.rect = self.rect = self.image.get_rect()
        else:
            #create a bullet rect at (0,0) and then set the correct position
            self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        """draw bullet to the screen"""
        if self.heihei:
            self.screen.blit(self.image, self.rect)
        else:    
            pygame.draw.rect(self.screen, self.color, self.rect)

        
        
