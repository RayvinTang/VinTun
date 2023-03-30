class Dog :
	def __init__(self, name):
		self.name = name
		self.age = 0
		self.isCute = True

	def roll_over(self):
		print(f"{self.name} rolled over...")

	def sleeping(self):
		print(f'{self.name} : "zzz..."')

	def barking(self):
		print(f'{self.name} : "Grrr..."')
'''
moly = dog("Moly")
print(moly.name)
print(moly.age)
print(moly.isCute)

holy = dog("Holy")
print(holy.name)
'''
daisy = Dog("Daisy")
print(daisy.name)
print(daisy.age)
print(daisy.isCute)
print(daisy.roll_over)
print(daisy.sleeping)
print(daisy.barking)