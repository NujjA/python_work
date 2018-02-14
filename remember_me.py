import json

#load user if stored
#otherwise store user if new

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
         username = input("Enter your name: ")
         with open(filename, 'w') as f_obj:
             json.dump(username, f_obj)
             print("Welcome to the system " + username)
else:
    print("Welcome back " + username)
