
#alien_0 = {'color': 'green', 'points':5}

#print(alien_0['color'])
#print("you just earned " + str(alien_0['points']) + " points!")

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25

#print("The alien is located at " + str(alien_0['x_position']) + ", " + str(alien_0['y_position']))

favorite_languages = {'Najla':'French',
                    'Roni':'Spanish',
                    'Zara': 'English',
                    'Saria':'monkey',
                    'Beejul':'English'}

adults = ['Roni', 'Najla']
kids = ['Zara', 'Saria']
for key,value in favorite_languages.items():
    print("\nKey: " + key.title())
    print("Value: " + value.title())
    if key in kids:
        print("Hi kiddo!")
        

#default behavior is to loop through just the keys
for name in favorite_languages:
    if name in adults:
        print("Good adulting " + name)

#set() will not have repeats
for language in set(favorite_languages.values()):
    print(language)
        
