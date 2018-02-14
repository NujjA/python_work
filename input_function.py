name = "start"
while True:   
    name = input("What is your name: ")
    if name == 'quit':
        break
    print("Hello " + name)
    age = input("How old are you?: ")
    age = int(age)
    if age < 18:
        print("You are a kid")
    else:
        print("You are not a kid")
