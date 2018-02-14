import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to keypress"""
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True    
    elif event.key == pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
 
def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    

def update_screen(ai_settings, screen, ship, alien, bullets):
    """update images on the screen and flip to a new screen"""
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
        
    ship.blitme()
    
    alien.draw(screen)

    #make the most recently drawn screen visible
    pygame.display.flip()
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """fire bullet if limit is not reached yet"""
    #create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
   
def update_aliens(ai_settings, aliens):
    """update the position of all aliens in the fleet, drop fleet if needed"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
def update_bullets(aliens, bullets):
    """update position of bullets and get rid of old bullets"""
    bullets.update()
        
    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    #check for any bullets that have hit aliens and if so get rid of bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen) #not part of fleet, just for sizing
    
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_of_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    
    #create fleet of aliens
    for row_number in range(number_rows):
        #create row of aliens
        for alien_number in range(number_aliens_x):
            #create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_of_rows(ai_settings, ship_height, alien_height):
    """determine number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    '''determine number of aliens that fit in a row'''
    available_space_x = ai_settings.screen_width - 2 * alien_width #one alien for each margin
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''create an alien and place it in the row'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    """respond appropriately if any aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    """drop entire fleet and change fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    