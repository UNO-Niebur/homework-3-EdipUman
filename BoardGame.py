# Homework 3 - Board Game System
# Name:
# Date:

import random

 """Reads game data from a file and returns it as a list."""
def load_game_data(filename):
    game_state = {"turn": "Player1", "players": {}, "events": {}}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(": ")
            if parts[0] == "Turn":
                game_state["turn"] = parts[1]
            elif "Player" in parts[1]:
                game_state["players"][parts[1]] = 1
            else:
                game_state["events"][int(parts[0])] = parts[1]
    return game_state

def save_game_data(filename, game_state):
    with open(filename, "w") as file:
        file.write(f"Turn: {game_state['turn']}\n")
        for player, position in game_state["players"].items():
            file.write(f"{position}: {player}\n")
        for space, event in game_state["events"].items():
            file.write(f"{space}: {event}\n")
    
"""Displays the current game state."""
def display_board(game_state):
    print("\n--- Current Game State ---")
    print(f"Current Turn: {game_state['turn']}")
    print("\nPlayers:")
    for player, pos in game_state["players"].items():
        print(f"  {player} is at position {pos}")
    print("\nEvents on Board:")
    for space, event in game_state["events"].items():
        print(f"  Position {space}: {event}")
 
def check_event(game_state, current_player):
    pos = game_state["players"][current_player]
    if pos in game_state["events"]:
        event = game_state["events"][pos]
        print(f"Event Triggered: {event}!")
        if event == "Treasure":
            game_state["players"][current_player] += 3
            print(f"  {current_player} Ye Matey found Treasure! Onward 3 spaces to look for more.")
        elif event == "Trap":
            game_state["players"][current_player] -= 2
            print(f"  {current_player} Ye be bamboozeled by a Trap! Reverse 2 spaces to gain ye bearing.")
        elif event == "Heal":
            game_state["players"][current_player] += 1
            print(f"  {current_player} Ye stumbled upon healing magic! Move forward 1 space with strength in ye.")

def switch_turn(game_state):
    players = list(game_state["players"].keys())
    current = game_state["turn"]
    idx = players.index(current)
    game_state["turn"] = players[(idx + 1) % len(players)]
    
 def move_player(game_state):
    current_player = game_state["turn"]
    roll = random.randint(1, 6)
    new_pos = game_state["players"][current_player] + roll
    if new_pos > 30:
        new_pos = 30
    game_state["players"][current_player] = new_pos
    print(f"\n{current_player} rolled a {roll} and moved to position {new_pos}.")
    check_event(game_state, current_player)
    if new_pos >= 30:
        print(f"\n{current_player} wins the game!")
        return game_state, True
    switch_turn(game_state)
    return game_state, False

def main():
    filename = "events.txt"
    game_state = load_game_data(filename)
 
    running = True
    while running:
        display_board(game_state)
        choice = input("\nMove player? (y/n) or 'q' to quit: ")
        if choice == "y":
            game_state, winner = move_player(game_state)
            save_game_data(filename, game_state)
            if winner:
                display_board(game_state)
                running = False
        elif choice == "n" or choice == "q":
            print("Closing game")
            running = False
 
if __name__ == "__main__":
    main()
