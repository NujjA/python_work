age = 100
youare = ""

if age < 2:
    youare = "a baby"
elif age < 4:
    youare = "a toddler"
elif age < 13:
    youare = "a kid"
elif age < 20:
    youare = "a teenager"
elif age < 65:
    youare = "an adult"
else:
    youare = "old AF"
    
print("You are " + str(age) + " and " + youare)
