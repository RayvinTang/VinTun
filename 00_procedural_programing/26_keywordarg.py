def describe_pet(animal_type, pet_name):

	print(f"I have a {animal_type}")
	print(f"my {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name="moliey", animal_type='pig')