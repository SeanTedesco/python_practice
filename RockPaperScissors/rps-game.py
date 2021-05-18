#######################################################################
# Imports
#
import random

#######################################################################
# globals
#
rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock']
    },
}

#######################################################################
# Functions
#
def show_header():
    print("-------------------------------")
    print("    Rock Paper Sciccors Game ")
    print("-------------------------------")

def get_roll(player_name, rolls):
    print("Available Rolls:")
    for i, r in enumerate(rolls, start=1):
        print(f"{i}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    index = int(text) - 1
    
    if index < 0 or index >= len(rolls):
        print(f"Sorry {player_name}, {text} is not in {rolls}")
        return None

    return rolls[index]

def check_for_win(p1, p2, r1, r2):

    winner = None

    if r1 == r2:
        print("The game is a tie!")

    outcome = rolls.get(r1, {})
    if r2 in outcome.get('defeats'):
        winner = p1
    elif r2 in outcome.get('defeated_by'):
        winner = p2

    return winner

def play_round(player_1, player_2):

    roll_keys = list(rolls.keys())

    roll2 = random.choice(roll_keys)

    roll1 = None
    while not roll1:
        roll1 = get_roll(player_1, roll_keys)

    print(f"{player_1} rolls {roll1}")  
    print(f"{player_2} rolls {roll2}")  

    winner = check_for_win(player_1, player_2, roll1, roll2)
    return winner

def find_winner(wins, names):
    best_of = 3
    for name in names: 
        if wins.get(name, 0) >= best_of:
            return name

def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}
   
    while not find_winner(wins, wins.keys()):
        winner = play_round(player_1, player_2)

        if winner == None:
            print("The round is a tie!")
        else: 
            print(f"Round winner is {winner}!")
            wins[winner] += 1

        print(f"The score is: {player_1}: {wins[player_1]} | {player_2}: {wins[player_2]}")
        print() 

    overall_winner = find_winner(wins, wins.keys())
    print(f"{overall_winner} wins the game!")
    return

#######################################################################
# Main
#
def main():
    show_header()
    player = input("Enter Player 1's name: ")
    ai = "Computer"
    play_game(player, ai)

if __name__ == '__main__':
    main()


