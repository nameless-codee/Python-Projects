import random 

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

number_to_guess = random.randint(lower_bound, upper_bound)

chances = 7
print(f"You have {chances} chances to guess the number between {lower_bound} and {upper_bound}.")

attempts = 0

while True:
    guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
    
    if guess < lower_bound or guess > upper_bound:
        print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
        continue

    attempts += 1
    if attempts < chances:
        if guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        break