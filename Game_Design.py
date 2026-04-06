Board: 30 spaces, players move forward by rolling a dice (1-6)
 
Rules:
- 2 players take turns rolling and moving forward
- Players start at position 1
- Landing on Treasure moves you forward 3 extra spaces
- Landing on Trap moves you back 2 spaces
- Landing on Heal moves you forward 1 extra space
- Event spaces are at positions 5, 12, 15, 18, 22, 27, and 29
- First player to reach space 30 wins
 
Functions:
- load_game_data: reads events.txt and returns a dictionary with turn, players, and events
- save_game_data: writes the updated game state back to events.txt
- display_board: prints the current game state showing player positions and events
- move_player: handles a full turn - dice roll, movement, events, and turn switching
- check_event: checks if the player landed on an event space and applies it
- switch_turn: switches to the next player's turn
- main: runs the program
 
Data Storage:
- events.txt stores turn, player positions, and event locations
- Inside the program data is stored as a dictionary with three keys:
  - turn: whose turn it is
  - players: dictionary of player names and their positions
  - events: dictionary of space numbers and event names
 
