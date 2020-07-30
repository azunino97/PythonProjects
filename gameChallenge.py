from random import randint

def guessingGame():
	"""
	Guess random integers from 1-100 where:

	A.	Guesses outside bounds return "OUT OF BOUNDS"
	B.	Turn 1:
			- Within 10 return "WARM!" else "COLD!"
		Turn 2+:
			- If guess is closer return "WARMER!" else "COLDER!"
	C.	When guessed correctly, return "You got it!  And it only took <guess_count> guesses!"
	"""

	guess = 0
	answer = randint(1,100)
	turn = 0
	distance = 0
	check = True
	outBounds = False

	print("Welcome to the Guessing Game! Guess an integer between 1-100 (inclusive)"\
		  " to get started: ")
	
	while check == True:
		try:
			guess = int(input())
		except ValueError:
			print("That's not an integer!")
			print("Guess again: ")
		else:
			check = False

	while(guess != answer):
		if turn >= 1 or outBounds == True:
			check = True
			outBounds = False
		else:
			check = False

		while check == True:
			try:
				guess = int(input())
			except ValueError:
				print("That's not an integer!")
				print("Guess again: ")
			else:
				check = False

		if guess > 100 or guess < 1:
			print('OUT OF BOUNDS')
			print('Guess again: ')
			outBounds = True
			continue

		if turn == 0:
			distance = abs(answer-guess)
			if distance <= 10:
				print("WARM!")
			else:
				print("COLD!")
			print("Next guess: ")

		if turn > 0:
			newdistance = abs(guess - answer)
			if newdistance < distance: 
				print("WARMER!")
			else:
				print("COLDER!")
			distance = newdistance
			print("Next guess: ")

		turn += 1


	print(f"You got it!  And it only took {turn} guesses!")

guessingGame()