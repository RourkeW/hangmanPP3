import random
import platform

print("Play HangMan!")

wordPool = ['front', 'sip', 'day', 'shorts', 'journal', 'alive', 'heel', 'film', 'carry', 'referee', 'burial', 'thinker', 'crown', 'branch', 'pan', 'exempt', 'dough', 'spy', 'dump', 'collect', 'water', 'license', 'closed', 'paper', 'wire', 'lobby', 'rib', 'posture', 'meaning', 'divide']
# neaten this
# perhaps find a genre for the toopic of these words i.e. gaming, cars...

# Choose the random word from the wordPool
randomWord = random.choice(wordPool)

for x in randomWord:
    print("_", end=" ")

# I need to find a way of making an underscore for each letter in the randomly chosen word and seperate them with a space so that the user can easily identify the amount of letters in the randomly chosen word to guess (for loop maybe?)

# function that will draw the hangman as the user guesses wrong
def draw_hangman(wrong_count):
    if(wrong_count == 0):
        print("\n------")
        print("|/   |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\___")
    elif(wrong_count == 1):
        print("\n------")
        print("|/   |")
        print("|    O")
        print("|")
        print("|")
        print("|")
        print("|\___")
    elif(wrong_count == 2):
        print("\n------")
        print("|/   |")
        print("|    O")
        print("|    |")
        print("|")
        print("|")
        print("|\___")
    elif(wrong_count == 3):
        print("\n------")
        print("|/   |")
        print("|    O")
        print("|    \|")
        print("|")
        print("|")
        print("|\___")
    elif(wrong_count == 4):
        print("\n------")
        print("|/   |")
        print("|    O")
        print("|    \|/")
        print("|")
        print("|")
        print("|\___")
    elif(wrong_count == 5):
        print("\n------")
        print("|/   |")
        print("|    O")
        print("|    \|/")
        print("|    /")
        print("|")
        print("|\___")
    elif(wrong_count == 6):
        print("\n------")
        print("|/   |")
        print("|    O")
        print("|    \|/")
        print("|    / \"")
        print("|")
        print("|\___")

# might have to switch which side the man hangs from

def show_word(correct_guesses):
    counter = 0
    correctLetters = 0
    for char in randomWord:
        if(char in correct_guesses):
            print(randomWord[counter], end=" ")
            correct_letters += 1
        else:
            print("_", end=" ")
            counter += 1
        return correct_letters

#function to discover letters

#function below shows the underscores for the randomWord chosen

def printWord():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")# found this online not sure whether to use this special character for the unknown letters

# After a meeting with my tutor I was advised to use a clear screen style to reproduce the game as it is played rather than risk having things stacked ontop of each other

def clear_screen():
    # remember to call this after each letter is guessed in the gamplay function
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("/033c", end="")
        else: 
            subprocess.run(["cls"])
    else:
        print("/033c", end="")

# Counter for the length of the word the player will guess
word_to_guess_length = len(randomWord)
# Wrong guess count starting at 0 since the game is starting
wrong_guess_count = 0
current_guess_index = 0
# current letters that have been guessed altogether
current_letters_guessed = 0
#letters guessed correctly counter
correct_letters = 0

while (wrong_guess_count != 6 and correct_letters != word_to_guess_length):
    print("\nLetters guessed so far: ") 
    for letter in current_letters_guessed:
        print(letter, end = " ")
    # User enters a letter now
    letter_guessed = input("\nPlease guess a letter")
    # Correct
    if(randomWord[current_guess_index] == letter_guessed):
        draw_hangman(wrong_guess_count)
        current_guess_index += 1
        # Add the letter to the array so the user wont guess it again
        current_letters_guessed.append(letter_guessed)
        correct_letters = show_word(current_letters_guessed)
        printWord()
    # Incorrect
    else:
        wrong_guess_count += 1
        current_letters_guessed.append(letter_guessed)
        draw_hangman(wrong_guess_count)
        correct_letters = show_word(current_letters_guessed)
        printWord()

print("Game is over")