# This game is written in Python 3.6.
# Author: Michael Xi

def hangman(word):
    welcome = input("Welcome to Hangman! Do you want to proceed? (y/n)\n")
    if welcome not in ["y", "Y"]:
        print("Exiting now")
        return
    life = 6
    # missing_word is used to compare how close our guessed word is to the real one
    missing_word = "*"*len(word)
    correct_guess = []
    while life > 0:
        print(missing_word)
        if missing_word == word:
            print("Congratulations! You Win!")
            return
        guess = input("Make your best guess, enter a letter\n")
        while len(guess) != 1:
            guess = input("Please only enter a letter\n")
        if guess in word:

            if guess not in correct_guess:
                missing_word = update_missing_word(missing_word,word,guess)
                print_graphic(life)
                correct_guess.append(guess)
            else:
                print("Make another guess!")
        else:
            life -= 1
            print("Wrong guess, you have "+str(life)+" life left.")
            print_graphic(life)
    print("GAME OVER")
    return


# This function is dedicated to print out the graphic of hangman.
def print_graphic(life):
    diff = 6-life
    graphic = [["________\n|      |"],
               ["________\n|      |\n|      0"],
               ["________\n|      |\n|      0\n|     /"],
               ["________\n|      |\n|      0\n|     /|"],
               ["________\n|      |\n|      0\n|     /|\ "],
               ["________\n|      |\n|      0\n|     /|\ \n|     /"],
               ["________\n|      |\n|      0\n|     /|\ \n|     / \ \nYou are dead."]]
    print(graphic[diff][0])
    return


def update_missing_word(missing_word, word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            missing_word = missing_word[0:i]+guess+missing_word[i+1:]
    return missing_word


# "microquest" will be the word we are guessing. You can replace it with any word you want.
# I assume all letters are lowercased.
hangman("microquest")
