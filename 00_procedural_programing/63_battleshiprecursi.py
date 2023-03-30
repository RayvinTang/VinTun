import os
import random

def intro():
	try:
		os.system("cls")
		print("Welcome to BattleShip")
		res = int(input("Please input how many rows you wanna play : "))
		if res < 3 or res > 10 :
			print("You must input a number more than 2 or less than or equal 10.")
			input("ENTER to try again.")
			return intro()
		return res
	except ValueError as e:
		print(f"You must put an integer number!\nPython Error{e}")
		input("ENTER to try again.")
		return intro()

def setting_up_board(rows):
	board = []
	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("0")
		board.append(line)
	return board

def setting_up_ship_location(rows):
	location = str(random.randint(0, rows-1)), str(random.randint(0, rows-1))
	return list(location)

def printing_board(board):
	os.system("cls")
	for row in board:
		for item in row:
			print(item, end=" ")
		print()

def check_user_input():
		try:
			user_input = input("ENTER Ship location : ").split(" ")
		except ValueError as e:
			print(f"You must put an integer number!\nPython Error{e}")
			input("ENTER to try again.")
			return check_user_input()
		else:
			if len(user_input) != 2:
				return check_user_input()
			if int(user_input[0]) < 0 or int(user_input[1]) > rows-1 or int(user_input[1]) < 0 or int(user_input[1]) > rows-1:
				print(f"You must put number between 1 and {rows}")
				input("ENTER to try again.")
				return check_user_input()
			if my_ship == user_input:
				return True
			else:
				my_board[int(user_input[0])][int(user_input[1])] = "x"
				return False

def congrats():
	print(f"You Win! With {attempt} attempts.")

win = False
attempt = 1

rows = intro()
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)

while not win:
	printing_board(my_board)
	print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

congrats()
'''
	try:
		rows = int(intro())
	except ValueError as e:
		print(f"You must put an integer number!\nPython Error{e}")
		input("ENTER to try again.")
	else:
		if rows < 3:
			print("You must input a number more than 2.")
			input("ENTER to try again.")
		else:
			break

row = int(intro())
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)
while not win:
	printing_board(my_board)
	print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1
congrats()
'''