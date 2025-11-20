#Mini Project : Rock Paper Scissors

import random

class Game:
    def __init__(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()

    def get_user_item(self):
        # get and validate user input
        while True:
            user_input = input('Please select rock, paper or scissors: ').lower().strip()
            if user_input in ('rock', 'paper', 'scissors'):
                self.user_item = user_input
                return self.user_item
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        # generate computer's choice randomly
        items = ['rock', 'paper', 'scissors']
        self.computer_item = random.choice(items)
        return self.computer_item

    def get_game_result(self):
        # determine and return game result
        if self.user_item == self.computer_item:
            return "It's a tie!"
        elif (self.user_item == "rock" and self.computer_item == "scissors") or \
             (self.user_item == "paper" and self.computer_item == "rock") or \
             (self.user_item == "scissors" and self.computer_item == "paper"):
            return  "You win!"
        else:
            return "You lose!"
        
        

    def play(self):
        # ... code to get user and computer choices ...
        # user = self.get_user_item()
        # computer = self.get_computer_item()
        # ... code to determine game result ...
        result = self.get_game_result()
        # ... code to print game outcome ...
        print(f"You chose: {self.user_item}, computer chose: {self.computer_item}. {result}")
        return result
    
