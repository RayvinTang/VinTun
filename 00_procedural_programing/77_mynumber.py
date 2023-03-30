name = input()
my_number = 0
for char in name:
	my_number += ord(char)
print(my_number)
print("Inisial jodoh kamu: ", chr(my_number%26 + 65))