import random
import logging

logging.basicConfig(filename='std.log', level=logging.INFO)
logging.info('This will get logged to a file')
def  play_numbergame():
    highrange = int(input("Enter the Highest limit of the range: \n"))
    lowrange = int(input("Enter the Lowest limit of the range: \n"))
    n = random.randint(lowrange,highrange)
    guessnumber = 0
    while (guessnumber < 5):
        guess = int(input("Enter your guess: \n"))
        guessnumber = guessnumber + 1
        if (guess<n):
            print("Go Higher! \n")
        elif (guess>n):
            print("Go Lower! \n")
        elif (guess == n):
            break
    if guess == n:
        print ("You won in "+ str(guessnumber) + " tries")
        logging.info("You won in "+ str(guessnumber) + " tries")
    else:
        print(" You Lost")
        logging.info("You Lost")
