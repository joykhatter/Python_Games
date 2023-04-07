''' This is the main file. Run this file to select and play a particular
    game.'''

from rockpaperscissors import *
from numbergame import *
from tictactoe import *
from connect4 import *
from hangman import *

game_lib = {
    1: "Rock Paper Scissors",
    2: "Numbers game",
    3: "Checkers"
}
while True:
    print("""
Your game library:
1: Tic-Tac-Toe
2: Numbers Game
3: TictacToe
4. Connect 4
5. Hangman
""")
    game_choice = input("""
What game would you like to play?
Input the game ID, or type 'exit' to exit.
""")

    if game_choice == '1':
        play_rockpaperscissors()
        game_choice = None

    elif game_choice == '2':
        play_numbergame()
        game_choice = None

    elif game_choice == '3':
        play_tictactoe()
        game_choice = None

    elif game_choice == '4':
        play_connect4()
        game_choice = None
     
    elif game_choice == '5':
        hangman()
        game_choice = None

    elif game_choice == 'exit':
        break
