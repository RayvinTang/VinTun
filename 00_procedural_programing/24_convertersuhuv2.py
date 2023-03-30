import os

def cetak_pilihan():
	print("Pilihan Menu")
	print("'cf' konversi dari Celcius-Farenheit")
	print("'cr' konversi dari Celcius-Reamur")
	print("'ck' konversi dari Celcius-Kelvin")
	print("'fc' konversi dari Farenheit-Celcicus")
	print("'fr' konversi dari Farenheit-Reamur")
	print("'fk' konversi dari Farenheit-kelvin")
	print("'rc' konversi dari Reamur-Celcicus")
	print("'rf' konversi dari Reamur-Farenheit")
	print("'rk' konversi dari Reamur-Kelvin")
	print("'kc' konversi dari Kelvin-Celcicus")
	print("'kf' konversi dari Kelvin-Farenheit")
	print("'kr' konversi dari Kelvin-Reamur")
	print("'q' untuk keluar dari program")

def Celcius_ke_Farenheit(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32
def Celcius_ke_Reamur(suhu_c):
	return 4.0 / 5.0 * suhu_c
def Celcius_ke_Kelvin(suhu_c):
	return suhu_c + 273
def Farenheit_ke_Celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0
def Farenheit_ke_Reamur(suhu_f):
	return (suhu_f - 32) * 4.0 / 9.0
def Farenheit_ke_Kelvin(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0 + 273
def Reamur_ke_Celcius(suhu_r):
	return 5.0 / 4.0 * suhu_r
def Reamur_ke_Farenheit(suhu_r):
	return (9.0 / 4.0 * suhu_r) + 32
def Reamur_ke_Kelvin(suhu_r):
	return 5.0 / 4.0 * suhu_r + 273
def Kelvin_ke_Celcius(suhu_k):
	return suhu_k - 273
def Kelvin_ke_Farenheit(suhu_k):
	return (suhu_k - 273) * 9.0 / 5.0 + 32
def Kelvin_ke_Reamur(suhu_k):
	return 4.0 / 5.0 * (suhu_k - 273)

error = False
pilihan = None
while not error:
	os.system("cls")
	cetak_pilihan()
	pilihan = input("pilihan : ")
	if pilihan == 'cf':
		main_c = float(input("Suhu_Celciusnya : "))
		result = Celcius_ke_Farenheit(main_c)
		print(f"farenheit : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'cr':
		main_c = float(input("Suhu_Celciusnya : "))
		print(f"Reamur : {Celcius_ke_Reamur(main_c)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'ck':
		main_c = float(input("Suhu_Celciusnya : "))
		print(f"Kelvin : {Celcius_ke_Kelvin(main_c)}")
		input("Tekan ENTER untuk kembali ke Menu")
	if pilihan == 'fc':
		main_f = float(input("Suhu_Farenheitnya : "))
		print(f"Celcius : {Farenheit_ke_Celcius(main_f)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'fr':
		main_f = float(input("Suhu_Farenheitnya : "))
		print(f"Reamur : {Farenheit_ke_Reamur(main_f)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'fk':
		main_f = float(input("Suhu_Farenheitnya : "))
		print(f"Kelvin : {Farenheit_ke_Kelvin(main_f)}")
		input("Tekan ENTER untuk kembali ke Menu")
	if pilihan == 'rc':
		main_r = float(input("Suhu_Reamurnya : "))
		print(f"Celcius : {Reamur_ke_Celcius(main_r)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'rf':
		main_r = float(input("Suhu_Reamurnya : "))
		print(f"Farenheit : {Reamur_ke_Farenheit(main_r)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'rk':
		main_r = float(input("Suhu_Raemurnya : "))
		print(f"Kelvin : {Reamur_ke_Kelvin(main_r)}")
		input("Tekan ENTER untuk kembali ke Menu")
	if pilihan == 'kc':
		main_k = float(input("Suhu_Kelvinya : "))
		print(f"Celcius : {Kelvin_ke_Celcius(main_k)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'kf':
		main_k = float(input("Suhu_Kelvinya : "))
		print(f"Farenheit : {Kelvin_ke_Farenheit(main_k)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'kr':
		main_k = float(input("Suhu_Kelvinya : "))
		print(f"Reamur : {Kelvin_ke_Reamur(main_k)}")
		input("Tekan ENTER untuk kembali ke Menu")

print("bye bye..")



