import random
import logging

logging.basicConfig(filename='std.log', level=logging.INFO)
logging.info('This will get logged to a file')

def play_rockpaperscissors():
    fplayerW = 0
    splayerW = 0
    draw = 0
    cont = True
    while(cont == True):
        fplayer = input('Player - 1 - Input r, p, or s\n')
        splayer = random.choice(['r','p','s'])
        print("Second Player chose - "+ splayer)
        if(fplayer == 'r'):
            if(splayer == 'r'):
                print("Draw game")
                draw = draw + 1
            elif(splayer == 'p'):
                print("Player - 2 wins ") 
                splayerW = splayerW + 1  
            elif(splayer == 's'):
                print("Player - 1 wins ") 
                fplayerW = fplayerW + 1
        elif(fplayer == 'p'):
            if(splayer == 'p'):
                print("Draw game")
                draw = draw + 1
            elif(splayer == 's'):
                print("Player - 2 wins ") 
                splayerW = splayerW + 1   
            elif(splayer == 'r'):
                print("Player - 1 wins ") 
                fplayerW = fplayerW + 1
        elif(fplayer == 's'):
            if(splayer == 's'):
                print("Draw game")
                draw = draw + 1
            elif(splayer == 'r'):
                print("Player - 2 wins ") 
                splayerW = splayerW + 1   
            elif(splayer == 'p'):
                print("Player - 1 wins ") 
                fplayerW = fplayerW + 1
        print('Player 1 wins - '+ str(fplayerW) + ' Player 2 wins - '+ str(splayerW) + ' and Draw - ' + str(draw))
        logging.info('Player 1 wins - '+ str(fplayerW) + ' Player 2 wins - '+ str(splayerW) + ' and Draw - ' + str(draw))
        check = input('Do you want to play again Y for yes and N for  No\n')
        if (check == 'N'):
            cont = False