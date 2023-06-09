import json
import random

def saving_data(favorite_number):
	with open("data.json", "w") as file:
		json.dump(favorite_number, file)

def loading_data():
	with open("data.json", "r") as file:
		return json.load(file)

def get_stored_number():
	try:
		return loading_data()
	except:
		return

def get_by_guesssing():
	guessing_favorite_number = random.randint(0, 100)
	confirm_answer = input(f"I'll guess your favorite number is {guessing_favorite_number}, is it right? (y/n)")
	if confirm_answer.lower() == "y":
		return str(guessing_favorite_number)

def get_new_favorite_number():
	guessing_favorite_number = get_by_guesssing()
	if guessing_favorite_number:
		favorite_number = guessing_favorite_number
	else:
		favorite_number = input("So what is yor favorite number? ")

	saving_data(favorite_number)
	return favorite_number

def ask_user():
	favorite_number = get_stored_number()
	if favorite_number:
		print(f"I know your favorite_number, it's {favorite_number}")
	else:
		favorite_number = get_new_favorite_number()
		print(f"I'll remember, '{favorite_number}' is your favorite number")

ask_user()