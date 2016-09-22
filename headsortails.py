import random

number = random.randint(1, 100)
if number % 2 == 0:
	answer = "heads"
else:
	answer = "tails"

print("Secret answer = ", answer) # for testing
guess = input("Please make a guess, heads or tails: ")

if guess.lower().strip() == answer:
	print("You are correct!  Winner!")
else:
	print("You were wrong.  :(")