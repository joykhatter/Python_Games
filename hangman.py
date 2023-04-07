import random

# List of words to choose from
words = ["apple", "banana", "cherry", "orange", "pear", "watermelon"]

def hangman():
    # Set up the game
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    guessed_word = ["_"] * len(word)
    
    # Play the game
    while tries > 0:
        print(" ".join(guessed_word))
        print(f"You have {tries} tries left.")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            if "_" not in guessed_word:
                print("You win!")
                return
        else:
            print("Incorrect!")
            tries -= 1
        
        guessed_letters.append(guess)
    
    # Game over
    print(" ".join(guessed_word))
    print("You lose!")
    print(f"The word was {word}.")
