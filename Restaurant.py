class Restaurant():
    """This is a restuarant"""
    
    def __init__(self, name, cuisine, open_status):
        self.name = name
        self.cuisine = cuisine
        self.open_status = open_status
        
    def describe_restaurant(self):
        print(self.name + " is a restaurant that serves " + self.cuisine)
        self.check_status()
        
    def open_restaurant(self):
        self.open_status = True
        print(self.name + " is now open")
        
    def close_restaurant(self):
        self.open_status = False
        print(self.name + " is now closed")
        
    def check_status(self):
        word = "error"
        if(self.open_status):
            word = "open"
        else:
            word = "closed"
        print(self.name + " is currently " + word)
        

rest1 = Restaurant("La Cheese", "cheese", False)
rest1.describe_restaurant()
rest1.open_restaurant()
rest1.describe_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, open_status, flavors):
        super().__init__(name, cuisine, open_status)
        self.flavors = flavors
        
    def flavors_served(self):
        print("We serve the following flavors:")
        for flavor in self.flavors:
            print(flavor)
            
            
rest2 = IceCreamStand("La Glacee", "ice cream", False, ["vanilla", "chocolate", "peach"])
rest2.describe_restaurant()
rest2.open_restaurant()
rest2.flavors_served()
rest2.describe_restaurant()

        
        
