current_users = ['admin', 'kmelbone', 'acropora', 'cheesepants', 'blah']
#current_users = []

if current_users:
    for user in current_users:
        if user == 'admin':
            print("Hello admin, you smaaat thing you")
        else:
            print("Welcome " + user)
else:
    print("Where are all the users?")

new_users = ['kmelbone', 'gjir', 'rgijeo', 'blah']
for newuser in new_users:
    if newuser in current_users:
        print(newuser + " is taken, try again.")
    else:
        print("Welcome " + newuser)
