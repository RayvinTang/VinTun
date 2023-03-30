def get_question():
	return [
		["What color is the daytime sky on a clear day?", "blue"],
		["What is the answer to life, the universe and everything?", "42"],
		["What is a three letter word for mouse trap?", "cat"],
		["Where is Eiffel Tower located?", "paris"],
		["Am I a robot?", "yes"],
		["reCAPTCHA: Are you a robot?", "no"]
	]

def check_question(row):
	q = row[0]
	a = row[1]

	user_ans = input(q)
	if user_ans == a:
		print("Correct")
		return True
	else:
		print(f"Incorrect!, correct was : {a}")
		return False

def main(questionbank):
	if len(questionbank) == 0:
		print("No question were given")
		return None

	index = 0
	right = 0
	while index < len(questionbank):
		
		if check_question(questionbank[index]):
			right += 1
		index += 1
	print(f"Your score is {right/len(questionbank)*100}")

main(get_question())
