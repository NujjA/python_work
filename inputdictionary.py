responses = {}
polling_active = True

while polling_active:
    name = input("Enter your name: ")
    vacation = input("Where is your dream vacation?: ")
    more = input("Enter more users? (Y/N): ")
    
    responses[name] = vacation
    
    if more == 'N':
        polling_active = False
        

for name, vacation in responses.items():
    print(name + " would like to go to " + vacation)
