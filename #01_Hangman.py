## Based on PDF 'Programação em Python e Introdução ao Pygame' from Kaya Sumire Abe - Brazil: Federal College of Parana
import random
HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
==========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
==========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
==========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
==========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
==========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
==========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
==========''']

words = 'cat uncle baby sword dad mom school portuguese stairs mountain poop train orange banana zebra couch computer'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missesLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print("Missed letters:", end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
           blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please, enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter, choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvxy':
            print("Please, enter a LETTER")
        else:
            return guess

def playAgain():
    print("Do you want to play again? Yes or No")
    return input().lower().startswitch('y')

print("H A N G M A N")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! the secret word is '" + secretWord + "'! You have won!!")
            gameIsDone = True
            
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print("You have run out of gusses!\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guessesm the word was '" + secretWord + "'")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break








    




