BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}


def render(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])




def play_tictactoe():

    player = 'X'
    game_round = 0
    game_over = False
    board = None

    while (game_over == False):
        board = BOARD
        render(board)
        print("Turn -  " + str(game_round + 1) + "  Place -  " + player + " at position? (1-9)")
        choice = int(input())
        if (board[choice] == ' '):
            board[choice] = player
            game_round = game_round +1
        else:
            print ("position taken chse another")
            continue
        
        if (game_round>4):
            if board[1] == board[2] == board[3] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[4] == board[5] == board[6] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[7] == board[8] == board[9] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[1] == board[4] == board[7] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[2] == board[5] == board[8] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[3] == board[6] == board[9] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[1] == board[5] == board[9] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
            elif board[3] == board[5] == board[7] == player:
                print(player + " Wins")
                game_over = True
                render(board)
                break
        if game_round == 9:
            print("Tie game")
            game_over = True
        if player=="X":
            player = "O"
        else:
            player = "X"


        