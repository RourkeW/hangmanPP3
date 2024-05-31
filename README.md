# HangMan Game

![am-i-responsive](read.me_images/am_i_responsive.JPG)

This is a project based on the classic hangman game using words chosen at random by the import random module in python, I learnt alot in this project and had some good fun overcoming challenges whilst building it.

* The GitHub repository for this project can be found here https://github.com/RourkeW/hangmanPP3
* The project has been deployed on heroku, this can be found here https://hangmanpp3rw-07abbe2bff2a.herokuapp.com/

## How to play 
1. The game is set up by drawing empty gallows and the player is asked to guess the word or letter.
2. The player inputs a guess being a letter or a word(e.g. "A" or "E") I included a clause to detect if the word or letter has been guessed in the playthough so the user cannot make the same guess by mistake.
3. In classic hangman you have 6 incorrect guesses before the game is lost, I have chosen this approach too.
4. If a player guesses incorrectly then part of the hangman is drawn, (head, head and torso, head, torso and one arm, head torso, and both arms, head, torso, both arms and one leg and finally head, torso, botha rms and both legs(I did this using ascii and a array to redraw the hangman each time)
5. if the player makes a correct guess then the missing space filled with an underscore is filled in and theya re not penalised. 
6. If the player reaches 6 incorrect guesses then the game will end witha  game over message and there will be a prompt to restart the game and the user is informed of the word that was to be guessed.
7. If the player manages to guess the word by letter or the full word then a message will display to let them that they have won and there will be a prompt to restart the game, I did not make it so words are remove from the wordpool because I thought its better this way.

# Design of the game
![LucidChart](read.me_images/plan_hangman.png)
