"""Problem Statement

We are going to write a program that generates a random number and ask the user to guess it.
If the player's guess is higher than the generated number the program display--"Enter Lower num. please"
similarly if the user's guess is lower than  the generated number the program display--"Enter higher num. please"
when the user guesses the correct number, the program display the number of guesses the player used to arrive at the generated number."""

import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
