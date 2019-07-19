import random

word = input("Player 1, type out your word for player 2 to guess!")

# Converts the word to lowercase
word = word.lower()

# Creates a list that will keep track of what is correct so far
current_word = []

for i in range(len(word)):
	current_word.append("_")


# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	print(" ".join(current_word))
	print("You have guessed " + str(guesses) + " so far")

	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	while len(guess) != 1:
		print("Invalid input")
		guess = input("Guess a letter: ")

	while guess in guesses:
		print("You have already guessed this letter")
		guess = input("Guess a letter: ")

	guesses.append(guess)

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	if guess in word:
		for i in range(len(word)):
			if word[i] == guess:
				current_word[i] = guess
		if "_" not in current_word:
			print("You win!!!!")
			exit()
	else:
		fails = fails + 1
		print("You have " + str(maxfails - fails) + " tries left!")

print("You ran out of lives! You lose")
