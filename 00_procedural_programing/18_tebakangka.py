import random

angkaBenar  = random.randint(0,100)
tebakan = None

print("tebak angka!\n")
while tebakan != angkaBenar:
	tebakan = int(input("angkanya : "))

	if tebakan == angkaBenar:
		print("ya benar")
	elif tebakan < angkaBenar:
		print(f"angkanya lebih besar dari {tebakan} ")
	elif tebakan > angkaBenar:
		print(f"angkanya lebih kecil dari {tebakan} ")