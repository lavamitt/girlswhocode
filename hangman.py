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

# Main while loop
while fails < maxfails:
	
	#Prints the current solved word so far & guesses
	print(" ".join(current_word))
	print("You have guessed " + str(guesses) + " so far")

	guess = input("Guess a letter: ")

	# Check if the guess is valid: Is it one letter?
	while len(guess) != 1:
		print("Invalid input")
		guess = input("Guess a letter: ")

	# Have they already guessed it?
	while guess in guesses:
		print("You have already guessed this letter")
		guess = input("Guess a letter: ")

	guesses.append(guess)

	# Check if the guess is correct: Is it in the word? If so, reveal the letters!

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

# If exited out of the while loop, then we must have ran out of lives!
print("You ran out of lives! You lose")
