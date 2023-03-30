def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings: ")
	if toppings:
		for topping in toppings:
			print(f"\t-{topping}")

make_pizza()
make_pizza("cheese")
make_pizza("make_pizza", "mushrooms", "pepperoni")