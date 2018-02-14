import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """initialize ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load ship image and get its rect
        self.image = pygame.image.load('Moana_boat_small.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        #store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """update the ship's position based on the movement flag"""
        #update the ship's center value, not the rect
        #make sure doesnt go off the edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

            
        #update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
