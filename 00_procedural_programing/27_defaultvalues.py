def describe_pet(pet_name, animal_type = "dog"):

	print(f"I have a {animal_type}")
	print(f"my {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('willie')

#equivalent function
describe_pet('willie', 'dog')
describe_pet(animal_type='dog', pet_name='wilie')
describe_pet('willie')
describe_pet(pet_name='wilie', animal_type='dog')