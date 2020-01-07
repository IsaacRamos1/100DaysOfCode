# jogo da advinhação
import random

guessTaken = 0

print("Hello!, what's your name?")
myName = input()

number = random.randint(1, 20)
print("Well," + myName + ", I'm thinking of a number between 1 and 20.")

while guessTaken < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    elif guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken)
    print("Good Job, " + myName + "! You guessed my number in " + guessTaken + " guesses")
else:
    number = str(number)
    print("Nope, the number i thought was " + number)
