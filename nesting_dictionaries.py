alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

#make a lot of blue aliens
for alien_number in range(5):
    new_alien = {'color':'blue', 'points':1}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))

#change just the blue aliens
for alien in aliens:
    if alien['color'] == 'blue':
        alien['points'] = 2

for alien in aliens:
    print(alien)

