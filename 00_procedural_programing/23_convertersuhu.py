

def cetak_pilihan():
	print("Pilihan Menu")
	print("'c' konversi dari Celcius")
	print("'f' konversi dari Farenheit")
	print("'q' untuk keluar dari program")

def Celcius_ke_Farenheit(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32

def Farenheit_ke_Celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

pilihan = None
while pilihan != "q":
	cetak_pilihan()
	pilihan = input("pilihan : ")
	if pilihan == 'c':
		main_c = float(input("Suhu_Celcius-nya"))
		result = Celcius_ke_Farenheit(main_c)
		print(f"farenheit : {result}")
	elif pilihan == 'f':
		main_f = float(input("Suhu Farenheit-nya : "))
		print(f"Celcius : {farenheit_ke_Celcius(main_f)}")

print("bye bye..")

