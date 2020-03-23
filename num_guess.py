# This is a guess the numbers game
# Meatbag referemce is from KOTOR
#
#

import random

guessesTaken = 0

print('Hello Meatbag species known as a "Human". What is your name?')
myName = input()

number = random.randint(1, 20)
print(
    "Well "
    + myName
    + ", I am storing a number between 1 and 20 in my memory... what is it?"
)

while guessesTaken < 6:
    print("Take a Guess if you dare... Meatbag known as " + myName)
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("your guess is to low")

    if guess > number:
        print("your guess is to high")

    if guess == number:
        break

if guess + number:
    guessTaken = str(guessesTaken)
    print(
        "Excellent use of your pink matter Meatbag known as "
        + myName
        + "! You've guessed the correct number in "
        + str(guessesTaken)
        + " guesses!"
    )

if guess != number:
    number = str(guessesTaken)
    print(
        "No dice Meatbag known as "
        + myName
        + " the number I was thinking of was "
        + number
    )
