#bottom to top

time = int(input("Nilai : "))

if time >= 90:
	print("A")
elif time >= 80:
	print("B")
elif time >= 65:
	print("C")
else:
	print("D")

#top to bottom

if time < 65:
	print("D")
elif time < 80:
	print("C")
elif time < 90:
	print("B")
else:
	print("A")

