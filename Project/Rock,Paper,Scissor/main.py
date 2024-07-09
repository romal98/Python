# https://www.youtube.com/watch?v=eWRfhZUzrAc&t=219s

import random

def get_choices():
    player_choice = input("Enter a choice: ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices 

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Draw"
    elif player == "rock":
        if computer == "scissor":
            return "Rock smashes scissor! You Win!"
        else:
            return "Paper covers rock! You Died!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!" 
        else:
            return "Scissor cuts paper! You Died!"
    elif player == "scissor":
        if computer == "paper":
            return "Scissor cuts paper! You Win!"
        else:
            return "Rock smashes scissor! You Died!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)