#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

options = ["rock", "paper", "scissors"]
player_score = 0

def play_round():
    # Generate the game round code, validate the player's input and determine the outcome of the round
    global player_score
    game_round = random.choice(options)
    player_choice = input("Enter your choice: ")
    if player_choice not in options:
        print("Invalid choice")
        return
    print("Computer chose: " + game_round)
    if player_choice == game_round:
        print("It's a tie!")
    elif player_choice == "rock" and game_round == "scissors":
        print("You win!")
        player_score += 1
    elif player_choice == "paper" and game_round == "rock":
        print("You win!")
        player_score += 1
    elif player_choice == "scissors" and game_round == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
pass

def main():
    global player_score
    print("Welcome to Rock, Paper, Scissors!")
    # Generate the main game code, including the game loop and scoring logic, control player input, and provide appropriate feedback
    while True:
        play_round()
        print("Your score: " + str(player_score))
        play_again = input("Play again? (y/n): ")
        if play_again == "n":
            break
    print("Thanks for playing!")
pass

if __name__ == "__main__":
    main()
    


    
    
    



