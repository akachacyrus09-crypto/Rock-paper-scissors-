import random

def start():
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    while True:
        print("ROCK, PAPER, SCISSORS")
        computer_choice = random.choice(choices)
        user_choice = input('\nEnter your choice (rock, paper or scissors): ').lower()

        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        if user_choice == computer_choice:
            comment = 'Draw'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            comment = 'You won'
            user_score += 1
        else:
            comment = 'You Lose'
            computer_score += 1

        print(f'Computer: {computer_choice}\nYou: {user_choice}\n{comment}, \nYour score: {user_score} \nComputer Score: {computer_score}')

        again = input('Play again? y/n: ').lower()
        if again != 'y':
            break

start()
