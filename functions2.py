def make_sandwich(name, *toppings):
    print(name + " ordered a sandwich with: ")
    for topping in toppings:
        print(topping)


make_sandwich("najla", "cheese", "eggs", "spinach")
make_sandwich("zara", "cheese", "turkey")
