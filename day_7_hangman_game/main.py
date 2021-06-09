import random
from hangman_art import stages, logo
from hangman_words import word_list

print("Welcome to Hnagman game")
print(logo)

lives = 6

word = random.choice(word_list)
word_len = len(word)

#list creation for storing the no. of dashesh in place of no. of words and then replacing it with letters
display = []

for digit in range(word_len):
    display += "_"
#defining a variable for a while loop to check if the player has worn and flaping it when the user wins or looses
end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ")

    if guess in display:
        print(f"The letter {guess} you have already chosen")

    for position in range(word_len):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in word:
        print("Letter {guess} is not in the word ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])

    
   

    



