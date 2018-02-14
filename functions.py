names = ['najla', 'roni', 'zara', 'saria']
adults = ['najla', 'roni']
people = []

def hello_function(name, shirt_size = "S"):
    """hello function"""
    print("Hello " + name)
    person = {}
    person[name] = shirt_size
    return person    

for name in names:
    person = {}
    if name in adults:
        person = hello_function(name, shirt_size = "L")
    else:
        person = hello_function(name)
    people.append(person)
    
print(people)
