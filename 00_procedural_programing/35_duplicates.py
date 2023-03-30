'''
daftarangka = [7, 8, 5, 1, 3, 3, 5, 7]
daftarangka.sort()
prev = None
for angka in daftarangka:
	if prev == angka:
		print(f"angka {angka} duplikat")
	prev = angka
'''
'''
req_toppings = ['mushroom', 'cheese', 'green peppers', 'pineapple']

req_customer = input("Add your topping : ")

if req_customer in req_toppings:
	print(f"Adding {req_customer} dan working your pizza!")
else:
	print(f"Sorry,we are run out of {req_customer} right now.")
'''
available_toppings = ['mushroom', 'olives', 'pepperoni', 'pineapple', 'cheese']

requested_toppings = []
stop = False
while not stop:
	topping = input("Input your topping here ('q' to quit): ")
	if topping != 'q':
		requested_toppings.append(topping)
	else:
		stop = True

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}")	

print("\nFinished making your pizza.")