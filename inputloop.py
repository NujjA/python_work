prompt = "Enter a pizza topping: "
toppings = []
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    toppings.append(topping)

print("The toppings you chose are: ")
for topping in toppings:
    print(topping)


while toppings:
    popped = toppings.pop()
    print("Putting " + popped + " on the pizza")
