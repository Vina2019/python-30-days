# Guess the number game

import random

No = random.randint(1, 10)

while True :
    guess = int(input("Guess the no from 1 to 10 : "))

    if No == guess:
        print("you guess the right no")

    else :
        print("Sorry try again")
