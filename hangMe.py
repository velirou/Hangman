import random

word_type = ''

#used to select a random type
sequence =  ['int', 'float', 'list', 'tuple', 'dict', 'str', 'set']

score = 0
highscore = 0

#filename for highscore
#you can change that
fn = 'highscore.txt'

#guesses history
previous = []

#used to hang the human
head = ''
upper_body = ''
lower_body = ''
left_arm = ''
right_arm = ''
left_foot = ''
right_foot = ''

#used for adding body parts
level = 0

def GenerateWord():
    #choose randomly from types
    global word_type
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
        #I use - instead of _ cause underscore is valid input
        hidden_word.append('-')
    return hidden_word

def ReadChar():
    letter = input("Guess: ")
    #print(letter)
    if len(letter) == 1 and letter.isalpha() or letter == '_':
        #uppercase or lowercase both correct
        letter = letter.lower()
        return letter
    else:
        print("Only single charachters are valid")
        return -1

def PreviousGuess(guess):
    if guess in previous:
        print("You already tried that charachter. Try again")
        return True
    return False

#7 wrong guesses and you loose
def Hang():
    global level, head, left_arm, upper_body, right_arm, lower_body, left_foot, right_foot
    if level == 0:
        return 0
    elif level == 1:
        head = 'O'
        return head
    elif level == 2:
        upper_body = '|'
        return upper_body
    elif level == 3:
        lower_body = '|'
        return lower_body
    elif level == 4:
        left_arm = '\\'
        return left_arm
    elif level == 5:
        right_arm = '/'
        return right_arm
    elif level == 6:
        left_foot = '/'
        return left_foot
    elif level == 7:
        right_foot = '\\'
        return right_foot
    else:
        print("Something went wrong with levels")

#used to print graphics
def HangTheHuman():
    global head, left_arm, upper_body, right_arm, lower_body, left_foot, right_foot
    print("------\n|    |\n|    " + head + "\n|   " + left_arm  + upper_body + right_arm  + "\n|    " + lower_body +  "\n|   " + left_foot + " " + right_foot)


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
        global level
        level += 1
    return hidden_word

#if max save highscore
def SaveHighscore():
    global score
    global highscore
    #read highscore or create highscore
    try:
        f = open(fn, 'r')
        highscore = int(f.read())
        print("Best score (highscore) is:", highscore)
        f.close()
    except IOError:
        f = open(fn, 'w')
        f.close()
    if score >= highscore:
        f = open(fn, 'w')
        f.write(str(score))
        f.close()
    #print("Current Highscore is:", score)

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

def InitializeHang():
    global head, left_arm, upper_body, right_arm, lower_body, left_foot, right_foot
    head = ''
    upper_body = ''
    lower_body = ''
    left_arm = ''
    right_arm = ''
    left_foot = ''
    right_foot = ''

#main loop
while True:

    #guesses history
    previous = []

    #word generator
    word = GenerateWord()

    #this is the given word. REMOVE THIS!
    print("This is the word you want to find:", word)

    #test show human
    #HangTheHuman(head, left_arm, upper_body, right_arm, lower_body, left_foot, right_foot)
    HangTheHuman()

    #word = GenerateWord()
    hidden_word = HideWord(word)
    PrintList(hidden_word)

    #main loop
    while True:

        #start printing new attempt
        print("========================================>")

        #read character
        guess = ReadChar()

        '''check if character is valid
           if no discart input and continue
           otherwise append previous guess
        '''
        if guess == -1:
            continue
        else:
            if PreviousGuess(guess) == True:
                continue

        #save history
        previous.append(guess)

        #check if guess is right
        hidden_word = CheckChar(word, hidden_word, guess)

        #hang
        Hang()
        HangTheHuman()

        #print history
        print("Previous guesses are:")
        PrintList(previous)

        #check if he lost the game
        if level >= 7:
            print("DEFFEAT")
            print("The word was:", word, "from", word_type)
            #also zero current score
            score = 0
            #also zero level flag again
            level = 0
            InitializeHang()
            break

        #check if he won the game
        if ChickenDinner(word, hidden_word):
            PrintList(hidden_word)
            print("Victory Royale")
            print("Your score is: ", score)
            SaveHighscore()
            break

        PrintList(hidden_word)
