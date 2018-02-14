
people = []

Roni = {'name':'Roni',
        'color':['orange']}
Zara = {'name':'Zara',
        'color':['purple', 'green']}
Najla = {'name':'Najla',
        'color':['gray', 'grey']}
Saria = {'name':'Saria',
        'color':['red', 'pink', 'white', 'blue']}

people.append(Roni)
people.append(Najla)
people.append(Zara)
people.append(Saria)

for person in people:
    print("Favorite colors for " + person['name'])
    for fav_colors in person['color']:
        print(fav_colors)
