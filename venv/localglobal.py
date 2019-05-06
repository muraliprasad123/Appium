# These is ro guess the random number
import random
secretNumber= random.randint(1,20)
print(" i am thinking a random number between 1 to 20")
# Ask the player to guess 6 times
for guesstime  in range(1,7):
    print("take Guess")
    guesstime =int(input())
    if guesstime < secretNumber:
        print("your guess is too low")
    elif guesstime> secretNumber:
        print("Your guess is too high")
    else:
        break


if guesstime == secretNumber:
    print("congrats you  guessed my number "+str(guesstime) + "guesses!")
else :
    print("sorry the number i was thinking of was "+str(secretNumber))



