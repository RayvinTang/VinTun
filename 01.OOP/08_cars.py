class Car:

	def __init__(self, make, model, year, color, new, manual):
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.new = new
		self.manual = manual
		self.odometer = 0

	def get_descriptive(self):
		return f"This car is a {self.make}'s car.\nIts model is {self.model}-{self.year}.\nIt has {self.color} color."

	def increment_odometer(self, kms):
		self.odometer += kms
		print(f"The odometer has been updated to {self.odometer}kms.")

	def fill_gas_tank(self):
		print(f"The car is full of fuell right now!")

	def change_color(self, new_color):
		self.color = new_color
		print(f"The color has been updated to {self.color}.")

class ElectricCar(Car):

	def __init__(self, make, model, year, color, new, manual):
		super().__init__(make, model, year, color, new, manual)
		self.battery = {"capacity" : 100, "size" : 5000}

	def fill_gas_tank(self):
		print("This car doesn't need a gas.")

	def charge_battery(self):
		print("This car is fully charged.")

hyundai = ElectricCar("hyundai", "kona ev", 2020, "black", True, False)
print(hyundai.get_descriptive())
hyundai.fill_gas_tank()
hyundai.charge_battery()

'''
toyota = Car("toyota", "yaris", 2020, "black", True, True)
print(toyota.get_descriptive())
toyota.increment_odometer(100)
toyota.fill_gas_tank()
toyota.change_color("blue")
'''			