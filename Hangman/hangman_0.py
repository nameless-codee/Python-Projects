import random

# List of words to guess
words = ["apple", "banana", "cherry", "date", "elderberry", 
         "fig", "grape", "honeydew", "kiwi", "lemon", "mango", 
         "nectarine", "orange", "papaya", "quince", "raspberry", 
         "strawberry", "tangerine", "ugli", "vanilla", "watermelon", 
         "xigua", "yam", "zucchini", "apricot", "blueberry", "cantaloupe",
         "dragonfruit", "eggplant", "feijoa", "guava", "jackfruit",
         "kumquat", "lime", "mulberry", "nectar", "olive", "peach",
         "pear", "plum", "pomegranate", "quinoa", "rhubarb", "starfruit",
         "tomato", "zest"]

# Randomly choose a word from the list
word_to_guess = random.choice(words)

# Welcome message and the spaces
print("\nWelcome to Hangman!")
print("Guess the following spaces!\n")

for space in word_to_guess:
    print("_", end=" ")

print('\n\nHint: It is a name of a fruit.')

# Setting variables
chances = len(word_to_guess) + 5
letter_guessed = ''
strike = 0

print(f'\nYou have {chances} chances, and 5 strikes to guess', end='')

while chances != 0:

    # Inputs a single character. If number is typed, it will do the 'except' part
    try:
        guess = str(input("\n\nGuess a letter: ")).lower()
    except:
        print('Enter only a letter!', end='')
        continue
    
    # Validation of the guess
    if not guess.isalpha():
        print('Enter only a LETTER', end='')
        continue
    elif len(guess) > 1:
        print('Enter only a SINGLE letter', end='')
        continue
    elif guess in letter_guessed:
        print("You've already guessed it!", end='')
        continue

    letter_guessed += guess
    flag = 0

    for letter in word_to_guess:
        if letter in letter_guessed:
            print(letter, end=' ')
            flag += 1
        else:
            print('_', end=' ')
    
    if guess not in word_to_guess:
        strike += 1
        print(f'\n\nStrike {strike}', end='')

    if flag == len(word_to_guess) :
        print('\n\nCongratulations!\n')
        break

    if strike == 5:
        print('\n\nMan is hanged!')
        print(f'The word was {word_to_guess}\n')
        break
    
    chances -= 1

if chances == 0:
    print('\n\nYou lost all the chances try again!')
    print(f'The word was {word_to_guess}\n')