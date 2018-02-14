import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Moana Sail Game")
    
    #make a ship
    ship = Ship(ai_settings, screen)
        
    #start the main loop for the game
    while True:
        
        #watch for keyboard and mouse movements, update ship accordingly
        gf.check_events(ship)
        ship.update()
                
        #redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship)
        
        #make the most recently drawn screen visible
        pygame.display.flip()
        
run_game()
