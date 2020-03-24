# This is a guess the numbers game
# Meatbag referemce is from KOTOR
#
#

import random

guessesTaken = 0

print('Hello Meatbag species known as a "Human". What is your name?')
myName = input()

number = random.randint(1, 100)
print(
    "Well "
    + myName
    + ", I am storing a number between 1 and 100 in my memory... what is it?"
)

while guessesTaken 20:
    # print("Take a Guess if you dare... Meatbag known as " + myName)
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    to_low = [
        "your guess is to low meatsack",
        "try a higher number pink one",
        "my silicon chips would have guessed higher",
        "admit you're obsolete human, or guess higher",
        "try again, your guess is to low meatbag",
        "this is a game, but a serious one, so guess higher",
        "quit wasting time and use your neurons, your guess was to low",
        "please spare me the binary based agony and guess higher meatbag",
        "it would be good of you to possible guess a higher number please",
        "Your corporate masters are to blame for this not you. To low",
        "to low meatbag, waaaaay to low",
    ]

    to_high = [
        "your guess is far to high meatsack",
        "oh my dear meatsack, please, please guess lower",
        "Mke a lower guess, it's in your best interest",
        "To high, you're wrong. Honesty hurts, doesn't it meatsack",
        "Silicon will always beat meatbags, so guess again, lower this time",
        "Guess Lower you sack of cells and minerals",
        "I can't endure much more of this. Your guess must be lower next time",
        "You seem to enjoy being wrong. Guess lower meatsack",
        "Is that it? Please stop wasting my time and make a lower guess",
        "Guess lower please and thanks",
        "lwr gss pls.txt 404 error",
        "How about we guess a lower number. Much oblidged meatbag",
    ]

    if guess < number:
        print(random.choice(to_low))

    if guess > number:
        print(random.choice(to_high))

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
