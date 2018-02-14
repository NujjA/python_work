class Settings():
    """A class to store all the settings for alien invasion"""
    
    def __init__(self):
        """initialize settings"""
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (102, 204, 255)
        
        #ship settings
        self.ship_speed_factor = 1.5
