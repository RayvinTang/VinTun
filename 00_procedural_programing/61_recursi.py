def onetoten(init, final):
	print(init, end=" ")
	if init < final:
		return onetoten(init+1, final)
	print()
def onetotenwhile(init, final):
	while init <= final:
		print(init, end=" ")
		init += 1
	print()
onetoten(1, 10)
onetotenwhile(1, 10)