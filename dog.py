class Dog():
    """Dog class"""
    
    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """dog sits"""
        print(self.name.title() + " is sitting")
        
    def roll_over(self):
        """dog rolls over"""
        print(self.name.title() + " rolls over")
        
        
        

my_dog = Dog('Bones', 3)

print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age))

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Poopy', 5)

your_dog.sit()
your_dog.roll_over()
