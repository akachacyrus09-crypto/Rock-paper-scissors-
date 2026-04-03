from nicegui import ui
import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def play_game(self):
        user_choice = self.user_input.value.lower()
        computer_choice = random.choice(self.choices)
        
        if user_choice not in self.choices:
            self.result.content = "Invalid choice! Try again."
            return
        
        if user_choice == computer_choice:
            comment = 'Draw'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            comment = 'You won'
            self.user_score += 1
        else:
            comment = 'You Lose'
            self.computer_score += 1
        
        self.result.content = (
            f'Computer: {computer_choice}\n\n'
            f'You: {user_choice}\n\n'
            f'**{comment}**\n\n'
            f'Your score: {self.user_score}\n\n'
            f'Computer Score: {self.computer_score}'
        )

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result.content = ''
        self.user_input.value = ''

game = Game()
with ui.column():
    ui.label('ROCK, PAPER, SCISSORS')
    game.user_input = ui.input('Enter your choice (rock, paper or scissors)')
    ui.button('Play', on_click=game.play_game)
    game.result = ui.markdown('')
    ui.button('Reset', on_click=game.reset_game)

ui.run()
