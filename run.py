import random

print("Play HangMan")

wordPool = ['front', 'sip', 'day', 'shorts', 'journal', 'alive', 'heel', 'film', 'carry', 'referee', 'burial', 'thinker', 'crown', 'branch', 'pan', 'exempt', 'dough', 'spy', 'dump', 'collect', 'water', 'license', 'closed', 'paper', 'wire', 'lobby', 'rib', 'posture', 'meaning', 'divide']
# neaten this
# perhaps find a genre for the toopic of these words i.e. gaming, cars...

# Choose the random word from the wordPool
randomWord = random.choice(wordPool)

# I need to find a way of making an underscore for each letter in the randomly chosen word and seperate them with a space so that the user can easily identify the amount of letters in the randomly chosen word to guess (for loop maybe?)

# function that will draw the hangman as the user guesses wrong
def draw_hangman(wrong_count):
    if(wrong_count == 0):
        print("\n------")
        print("|/")
        print("|")
        print("|")
        print("|\___")
    elif(wrong_count == 1):
    elif(wrong_count == 2):
    elif(wrong_count == 3):
    elif(wrong_count == 4):
    elif(wrong_count == 5):
    elif(wrong_count == 6):

