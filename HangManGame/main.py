#from replit import clear
import random
from hangman_words import word_list
from hangman_art import logo, stages

''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

print(logo)
print("\nWelcome to hangman")

# Select a random word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
	display.append("_")


while not end_of_game:
	# Get user input
    guess = input("Guess a letter: ").lower()
    isMaches = False
    #clear()
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You have already guessed {guess} in the past")
      continue

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            isMaches = True

    # Check if user is wrong.
    if not isMaches:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the chosen word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the stage of live
    print(stages[lives])
