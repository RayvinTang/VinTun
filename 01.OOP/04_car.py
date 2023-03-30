class Car:
	def __init__(self, brand, color, height):
		self.brand = brand
		self.color = color
		self.height = height

	def describe_car(self):
		print(f"{self.brand} is now on SALE. There are {self.color} available. It is a {self.height} car.")

etios_Valco = Car("Etios_Valco", "black", "short")
xenia = Car("Xenia", "silver", "tall")
jazz = Car("Jazz", "white", "short")
etios_Valco.describe_car()
xenia.describe_car()
jazz.describe_car()