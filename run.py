import random
from words import word_list
import subprocess
import platform

# Choose the random word from the wordPool
def get_word():
    word = random.choice(word_list)
    return word.upper()
#I chose to use the .upper() here since I want the answer to be more visible

# function that will draw the hangman as the user guesses wrong
def display_hangman(tries):
    stages = [  # in hangman, there are only 6 guesses usually so this is the end with the head, mid-section, both arms and both legs, message displays here to tell user that the game is over
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, mid-section and one leg comes when 5 guesses are wrong
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, mid-section and botha rms come when 4 guesses are wrong
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, mid-section and left arm come when 3 guesses are wrong
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso comes when 2 guesses are wrong
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head of the hanging man comes when 1 guess is wrong
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # game start here
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def clear_screen():
    """
    clearing screen for both windows/os users when called in other functions
    """
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:
        print("\033c", end="")

def play(word):
    # display the unguessed letters as underscores I make a string equal to the random word initially this is false of course
    word_completion = "_" * len(word)
    guessed = False
    # this array holds the letters a user has guessed so later I can make it so they cannot guess it again and I can not deduct a attempt count
    guessed_letters = []
    guessed_words = []
    tries = 6
    # Guides the user at the start
    print("Play HangMan!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    # main game loop below
    while not guessed and tries > 0:
        # again its .upper() I want to keep this constant
        guess = input("Please enter a guess or a word: ").upper()
        # I found out about this .isalpha() to check that a letter is a-z, this was found on W3 schools
        # first if is for letters
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried this letter", guess)
            elif guess not in word:
                print(guess, "is not in the hidden word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well Done,", guess, "is in the hidden word!")
                guessed_letters.append(guess)
                # This is how I am able to index correct letters over the underscores
                word_as_list = list(word_completion)
                # list comprehension and using enumerate, I did not learn this on code institute however I found it on various other sources and people have used it to count iterations when looping I wanted to try
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # I will now iterate over ythe indices to replace the letters when guessed correctly
                for index in indices:
                    word_as_list[index] = guess
                #now I am converting it back to a string
                word_completion = "".join(word_as_list)
                # it is possible that the guess completes the word but the user didnt type the word completely so I write if there are no underscores the game is done
                if "_" not in word_completion:
                    guessed = True
        # Below is the conditional for if the user just guesses a full word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried this word", guess)
            elif guess != word:
                print(guess, "is not the hidden word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Character not alowed.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else: # I saw on a coding video that you can use plus each side, I wanted to try it here
        print("Game Over! You ran out of attempts. The word was " + word + ".")

# This is the main function to run the game once and then promt for a play again
def main():
    word = random.choice(word_list)
    print("The length of the word to guess is :")
    print(len(word))
    word = get_word()
    play(word)
    while input("Try Again? (Y/N) ").upper() == "Y":
        #This above makes the function run as long as the user is clicking Y
        clear_screen()
        word = get_word()
        play(word)
# I found in another YouTube video that you can enter this and the script will run on the command line ASK TUTOR HERE
if __name__ == "__main__":
    main()