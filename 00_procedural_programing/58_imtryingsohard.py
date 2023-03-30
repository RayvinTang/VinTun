while True:
	a = input("a = ")
	b = input("b = ")
	try:
		res = int(a)/int(b)
	except ZeroDivisionError:
		print("You can't devide by zero!")
	except ValueError:
		print("You must put integer number!")
	else:
		print(f"a : b = {res}")
	finally:
		print("Done!")
	quit = input("Quit? (y/n)")
	if quit == "y":
		break