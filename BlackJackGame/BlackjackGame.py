############### Blackjack Project #####################



############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
from art import logo
#from replit import clear
import random

def blackjackGame():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  my_list = []
  computer_card_list = [] 
  # Select two random cards into my_list
  for _ in range(2):
    my_list.append(random.choice(cards))
    # Sum up my_list
  Sum = sum(my_list)
  print(f"Your cards: {my_list}, current score: {Sum}")

  # Select the first card for computer_list
  computer_card_list.append(random.choice(cards))
  computer_sum = sum(computer_card_list)
  print("Computer's first card: "+ str(computer_card_list[0]))

  if Sum < computer_sum:
    # Computer Win
    print(f"Your final hand: {my_list}, final score: {Sum}")
    print(f"Computer's final hand: {computer_card_list}, final score: {computer_sum}") 
    print("Lose, opponent has Blackjack 😱")
    return

  want_contd = True
  while want_contd and Sum <= 21:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'y':
      my_list.append(random.choice(cards))
      Sum = sum(my_list)
      # Replacing 11 with 1 incase Sum exceeds 21
      if Sum > 21 and 11 in my_list:
        Sum -= 10 
      print(f"Your cards: {list}, current score: {Sum}")
      print(f"Computer's first card: {computer_card_list[0]}")
    else:
      want_contd = False

  # Until the computer_sum is 17, select multiple cards for computer
  while computer_sum < 17:
    computer_card_list.append(random.choice(cards))
    computer_sum = sum(computer_card_list)

  if Sum > 21:
    print(f"Your final hand: {my_list}, final score: {Sum}")
    print(f"Computer's final hand: {computer_card_list}, final score: {computer_sum}") 
    print("You went over. You lose 😭")

  elif computer_sum > 21:
    # Computer lose
    print(f"Your final hand: {my_list}, final score: {Sum}")
    print(f"Computer's final hand: {computer_card_list}, final score: {computer_sum}") 
    print("Opponent went over. You win 😁")
  elif Sum > computer_sum:
    # I Win
    print(f"Your final hand: {my_list}, final score: {Sum}")
    print(f"Computer's final hand: {computer_card_list}, final score: {computer_sum}") 
    print("You win")
  elif Sum < computer_sum:
    # Computer Win
    print(f"Your final hand: {my_list}, final score: {Sum}")
    print(f"Computer's final hand: {computer_card_list}, final score: {computer_sum}") 
    print("Lose, opponent has Blackjack 😱")
  elif Sum == computer_sum:
  # Draw
    print("Draw")
  return
  



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':
  #clear()
  blackjackGame()