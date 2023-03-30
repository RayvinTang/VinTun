'''
this program made by :
Name : Rayvin Tang
Class : 10 Komputer 2
'''

import os
import random

#make custom battle ship intro,conggratz

def intro():
	print("Welcome to BattleShip Bootleg")
	return input("Rows size :")

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
	global attempt
	user_input = input("ENTER Ship location : ").split(" ")
	user_input = [str(int(user_input[0])-1), str(int(user_input[1])-1)]
	if my_ship == user_input:
		return True
	my_board[int(user_input[0])][int(user_input[1])] = "x"
	return False

def congrats():
	print(f"You Win! With {attempt} attempts.")

win = False
attempt = 1

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