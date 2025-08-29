import random

print("Welcome to my Number Guessing Game!")

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Enter Guess!"))

    if guess < number:
        print("Too Low! Guess Higher!")
    elif guess > number:
        print("Too High! Guess Lower!")
    else:
        print("You Won!")
