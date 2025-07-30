import random

choices = ['rock', 'paper', 'scissor']

print("\nWelcome to Rock, Paper, Scissors!")
print("You will play against the computer.\n")
print("If you want to exit the game, type 'exit'.")

com = 0
user = 0
turns = 0

def com_score():
    global com, turns, com_choice
    com += 1
    print(f'Because the computer chose {com_choice}')
    print(f'Computer score: {com}\n')
    turns += 1

def user_score():
    global user, turns, com_choice
    user += 1
    print(f'Because the computer chose {com_choice}')
    print(f'Your score: {user}\n')
    turns += 1

while turns < 11:
    com_choice = random.choice(choices)

    try:
        user_choice = input('Rock, Paper, Scissor shoot: ').lower()
    except:
        print('Please enter a valid choice!')
        continue

    if user_choice == 'exit':
        print('Exiting the game.')
        break

    if user_choice == com_choice:
        print(f"It's a tie! Both chose {com_choice}.\n")
        continue
    elif user_choice not in choices:
        print('Invalid choice! Please choose rock, paper, or scissor.')
        continue
    elif not user_choice.isalpha():
        print('Please enter only letters!')
        continue

    if user_choice == 'rock':
        if com_choice == 'paper':
            print('\nYou lose! Paper covers rock.')
            com_score()
        else:
            print('\nYou win! Rock crushes scissors.')
            user_score()
    elif user_choice == 'paper':
        if com_choice == 'scissor':
            print('\nYou lose! Scissors cut paper.')
            com_score()
        else:
            print('\nYou win! Paper covers rock.')
            user_score()

    elif user_choice == 'scissor':
        if com_choice == 'rock':
            print('\nYou lose! Rock crushes scissors.')
            com_score()
        else:
            print('\nYou win! Scissors cut paper.')
            user_score()

if com > user:
    print('Computer wins the game with,')
    print(f'Computer: {com}, You: {user}')
elif user > com:
    print('You win the game with,')
    print(f'Computer: {com}, You: {user}')