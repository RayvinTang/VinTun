''''
a_list = [
	[1, 2, 3, 4, 5],
	[6, 7, 8 , 9, 10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20]
]
'''
'''
for item in a_list:
	print(item, end=" ")
print()
'''
'''
for row in a_list:
	for col in row:
		print(col, end=" ")
	print()
'''
'''
stars = [
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"],
	["*", "*", "*", "*", "*"]
]
for row in stars:
	for star in row:
		print(star, end=" ")
	print()
'''

stars = []
rows = 5
cols = 5

for row in range(rows):
	line = []
	for col in range(cols):
		print("*", end=" ")
		line.append("*")
		stars.append(line)
	print()
for row in stars:
	for star in row:
		print(star, end=" ")
	print()