from random import randint
import random

#used to select a random type
sequence =  ['int', 'float', 'list', 'tuple', 'dict', 'str', 'set']

score = 0

#guesses history
previous = []

def GenerateWord():
    #choose randomly from types
    word_type = random.choice(sequence)
    #trim (underdocre)__functions then choose  randomly from rest methods
    possible_words = dir(word_type)
    for word in possible_words[:]:
        if word.startswith('_'):
            possible_words.remove(word)

    word = random.choice(possible_words)
    return word

def HideWord(word):
    hidden_word = []
    for letter in word:
        hidden_word.append('_')
    return hidden_word

def ReadChar():
    letter = input("Guess: ")
    #print(letter)
    if letter.isalpha():
        print("Input ok . . .")

        #uppercase or lowercase both correct
        letter = letter.lower()
        return letter
        print(letter, "+++++++++++++++++++++++++++++")
    else:
        print("Only single charachters are valid")
        return '0'

def PreviousGuess(guess):
    if guess in previous:
        print("You already tried that charachter. Try again")
        return True
    return False

def CheckChar(word, hidden_word, guess):
    found = False

    for idx, letter in enumerate(word):
        if guess == letter:
            hidden_word[idx] = letter
            found = True

    if found:
        print("Good Job")
    else:
        print("Sorry try again")
    return hidden_word

def ChickenDinner(word, hidden_word):
    #print(list(word))
    #print(hidden_word)
    if list(word) == hidden_word:
        global score
        score += 1
        return True
    return False

def PrintList(word):
    print(' '.join(word))


#second word generator
word = GenerateWord()

#this is the given word. REMOVE THIS!
print(word)

#word = GenerateWord()
hidden_word = HideWord(word)
PrintList(hidden_word)

#main loop
while True:
    guess = ReadChar()
    if PreviousGuess(guess) == True:
        continue

    previous.append(guess)

    hidden_word = CheckChar(word, hidden_word, guess)

    if ChickenDinner(word, hidden_word):
        PrintList(hidden_word)
        print("Victory Royale")
        print("Your score is: ", score)
        break

    PrintList(hidden_word)
