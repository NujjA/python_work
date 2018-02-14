import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #initialize and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Kakamora Attack")
    
    #make a ship
    ship = Ship(ai_settings, screen)
    
    #make a group to store bullets in
    bullets = Group()

    #fleet of aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
        
    #start the main loop for the game
    while True:
        
        #watch for keyboard and mouse movements, update ship and bullets accordingly
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        
        #redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        #make the most recently drawn screen visible
        pygame.display.flip()
        
run_game()
